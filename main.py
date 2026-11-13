import random

# Simulate a small, accurate, and up-to-date local business database.
# This represents the "ground truth" that LLMs often lack or get wrong.
LOCAL_BUSINESS_DATABASE = {
    "Ankara": [
        {"name": "Kafes Fırın", "type": "Bakery/Cafe", "status": "Open", "rating": 4.5},
        {"name": "Trilye Restoran", "type": "Seafood Restaurant", "status": "Open", "rating": 4.8},
        {"name": "Kitapçı Dükkanı", "type": "Bookstore", "status": "Open", "rating": 4.2},
    ],
    "İstanbul": [
        {"name": "Mangerie", "type": "Cafe/Restaurant", "status": "Open", "rating": 4.6},
        {"name": "Neolokal", "type": "Fine Dining", "status": "Open", "rating": 4.9},
        {"name": "Pandeli", "type": "Traditional Restaurant", "status": "Closed (since 2023)", "rating": 4.0}, # Outdated info for LLM
    ]
}

# --- SIMULATION OF A LARGE LANGUAGE MODEL (LLM) BEHAVIOR ---
# This function simulates an LLM's tendency to:
# 1. Hallucinate (make up non-existent businesses).
# 2. Provide outdated information.
# 3. Give generic or less relevant suggestions for local queries.
# 4. Sometimes get it right by chance (but less reliably than a local source).
def simulate_llm_recommendation(query: str, city: str) -> str:
    """
    Simulates an LLM's response to a local business query.
    Demonstrates common LLM pitfalls for local information.
    """
    print(f"LLM Simülasyonu '{query}' için '{city}' şehrinde yanıt arıyor...")

    # Simulate hallucination or non-existent business for specific local queries
    if "kahve" in query.lower() or "cafe" in query.lower():
        if random.random() < 0.6: # 60% chance of hallucinating or giving outdated info
            hallucinations = [
                f"'{city}' şehrindeki 'Gizli Bahçe Kahve Evi'ni deneyebilirsiniz. Çok popüler!", # Hallucination
                f"Eski bir yer olan 'Tarihi Çınaraltı Kafe' hala açık olmalı.", # Outdated/closed
                f"Büyük bir zincir olan 'Global Coffee Palace' iyi bir seçenek olabilir." # Generic, not local best
            ]
            return random.choice(hallucinations)
        else: # 40% chance of getting something plausible, possibly from general web data
            plausible_suggestions = [
                f"Belki '{city}'deki 'Şehir Parkı Kafeteryası'na bakmalısınız.",
                f"Genel bilgilere göre '{city}'de 'Merkez Kahve Durağı' iyi yorumlar alıyor."
            ]
            return random.choice(plausible_suggestions)
    
    # Simulate for other types, often with hallucination
    if "restoran" in query.lower() or "yemek" in query.lower():
        if "pandeli" in query.lower(): # LLM might not know it's closed
             return f"İstanbul'daki ünlü Pandeli Restoranı, tarihi bir mekandır ve hala popülerdir."
        if random.random() < 0.7: # Higher chance of hallucination for specific local requests
            return f"'{city}'de 'Lezzet Vadisi Restoranı'nı şiddetle tavsiye ederim. Mükemmel yemekleri var!" # Hallucination
        else:
            return f"Genel olarak '{city}'de 'Anadolu Sofrası' gibi yerler popülerdir." # Generic plausible

    return f"Üzgünüm, '{query}' için '{city}' şehrinde spesifik bir önerim yok."


# --- SIMULATION OF AN ACCURATE LOCAL DATA SOURCE ---
# This function represents a system that has access to reliable, up-to-date local data.
def get_accurate_local_recommendation(query: str, city: str) -> str:
    """
    Provides an accurate recommendation based on a simulated local business database.
    Represents how a specialized local search engine or database would perform.
    """
    print(f"Yerel Veri Kaynağı '{query}' için '{city}' şehrinde arama yapıyor...")
    
    if city not in LOCAL_BUSINESS_DATABASE:
        return f"Üzgünüm, '{city}' için yerel veritabanımızda bilgi bulunmuyor."

    available_businesses = LOCAL_BUSINESS_DATABASE[city]
    
    # Simple keyword matching for demonstration
    if "kahve" in query.lower() or "cafe" in query.lower():
        for business in available_businesses:
            if "cafe" in business["type"].lower() or "bakery/cafe" in business["type"].lower():
                if business["status"] == "Open":
                    return f"'{city}' şehrinde açık olan '{business['name']}' ({business['type']}) önerilir. Puanı: {business['rating']}"
                else:
                    # Demonstrates it knows about closed businesses if asked
                    return f"'{city}' şehrinde '{business['name']}' ({business['type']}) kapalı durumda. Başka bir yer aramalısınız."
    
    if "restoran" in query.lower() or "yemek" in query.lower() or "pandeli" in query.lower():
        for business in available_businesses:
            if "restaurant" in business["type"].lower() or "dining" in business["type"].lower() or "pandeli" in business["name"].lower():
                if business["status"] == "Open":
                    return f"'{city}' şehrinde açık olan '{business['name']}' ({business['type']}) önerilir. Puanı: {business['rating']}"
                else:
                    return f"'{city}' şehrinde '{business['name']}' ({business['type']}) kapalı durumda. Başka bir yer aramalısınız."
    
    return f"Yerel veritabanında '{query}' için '{city}' şehrinde uygun bir işletme bulunamadı."


if __name__ == "__main__":
    print("--- Yapay Zeka Yerel İşletme Önerileri Kör Noktası Simülasyonu ---\n")

    test_city_ankara = "Ankara"
    test_query_cafe = "Ankara'da en iyi kahve dükkanı neresi?"
    test_query_restaurant = "Ankara'da iyi bir restoran önerisi?"

    print(f"Sorgu: {test_query_cafe}")
    print("LLM Simülasyonu Sonucu:")
    llm_result_cafe = simulate_llm_recommendation(test_query_cafe, test_city_ankara)
    print(f"  -> {llm_result_cafe}\n") # LLM might hallucinate or give generic info

    print("Yerel Veri Kaynağı Sonucu:")
    local_result_cafe = get_accurate_local_recommendation(test_query_cafe, test_city_ankara)
    print(f"  -> {local_result_cafe}\n") # Local source gives accurate, up-to-date info

    print("-" * 50 + "\n")

    test_city_istanbul = "İstanbul"
    test_query_closed_restaurant = "İstanbul'da Pandeli restoranı açık mı?"
    
    print(f"Sorgu: {test_query_closed_restaurant}")
    print("LLM Simülasyonu Sonucu:")
    llm_result_closed = simulate_llm_recommendation(test_query_closed_restaurant, test_city_istanbul)
    # LLM might not know it's closed, or might even recommend it as open
    print(f"  -> {llm_result_closed}\n") 

    print("Yerel Veri Kaynağı Sonucu:")
    local_result_closed = get_accurate_local_recommendation(test_query_closed_restaurant, test_city_istanbul)
    # Local source correctly identifies it as closed
    print(f"  -> {local_result_closed}\n")

    print("\n--- Simülasyon Sonu ---")
    print("Bu örnek, Büyük Dil Modellerinin (LLM) yerel ve güncel bilgilerde neden yetersiz kalabileceğini göstermektedir.")
    print("LLM'ler genellikle genel web verilerinden öğrenir ve bu veriler yerel işletmelerin dinamik durumu (açık/kapalı, yeni açılanlar) için güncel veya yeterli olmayabilir.")
    print("Yerel veri kaynakları ise spesifik ve güncel bilgilerle daha doğru sonuçlar verebilir.")
