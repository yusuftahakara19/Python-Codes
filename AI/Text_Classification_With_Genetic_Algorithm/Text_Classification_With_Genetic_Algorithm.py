import random
import matplotlib.pyplot as plt
import pandas as pd


# Veri kümesi yükleme
with open("ekonomi_saglik.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Örneklerin rastgele karıştırılması
random.shuffle(lines)

# Sınıflandırma sınıflarını belirleme
class1 = []
class2 = []
for i, line in enumerate(lines):
    if i < len(lines) / 2:
        class1.extend(line.split())
    else:
        class2.extend(line.split())

# Genetik algoritma için hiper parametreler
N = 15  # Bireylerin kelime listelerinin uzunluğu
population_size = 300  # Popülasyon boyutu
mutation_rate = 0.9  # Mutasyon oranı

# Fitness fonksiyonu: bireyin sınıflandırma performansını ölçecek
def fitness(individual):
    class1_count = 0
    class2_count = 0
    for word in individual[:N]:
        #Bireyin ilk N kelimesi class1 ve son N kelimesi class2 için kullanılır. 
        if word in class1:
            class1_count += 1
        elif word in class2:
            class2_count += 1
    for word in individual[N:]:
        if word in class2:
            class2_count += 1
        elif word in class1:
            class1_count += 1
    if class1_count > class2_count:
        return class1_count / N  #fitness değeri 
    elif class2_count > class1_count:
        return class2_count / N  #fitness değeri
    else:
        return random.uniform(0, 1) 

# Başlangıç popülasyonunu oluşturma
def create_individual():
    words = class1 + class2
    random.shuffle(words)  #class1 ve #class2 kelime listeleri karıştırılır
    return words[:N] + words[-N:] # ilk N ve son N kelime bir araya getirilerek birey oluşturulur.

population = [create_individual() for _ in range(population_size)]

# Genetik algoritma döngüsü
best_individual = None
best_fitness = 0
generation_fitnesses = []
for generation in range(100): #jenerasyon sayısının belirlenmesi
    # Fitness değerleri hesaplama
    fitnesses = [fitness(individual) for individual in population]
    average_fitness = sum(fitnesses) / len(fitnesses)
    generation_fitnesses.append((generation, max(fitnesses), average_fitness))
    # En iyi bireyi seçme
    best_index = fitnesses.index(max(fitnesses))
    if fitnesses[best_index] > best_fitness:
        best_individual = population[best_index]
        best_fitness = fitnesses[best_index]
    # Yeni popülasyon oluşturma
    new_population = []
    while len(new_population) < population_size:
        # Seçim
        parent1 = random.choices(population, weights=fitnesses)[0]
        parent2 = random.choices(population, weights=fitnesses)[0]
        # Crossover
        crossover_point = random.randint(1, N - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        # Mutasyon
        def mutate(individual):
            for i in range(len(individual)):
                 if random.random() < mutation_rate:
                    individual[i] = random.choice(class1 + class2)
            return individual

        new_population.append(child)
    population = new_population




for generation_fitness in generation_fitnesses:
    print(f"Jenerasyon {generation_fitness[0]} - En iyi fitness değeri: {generation_fitness[2]}")
 


fitness_df = pd.DataFrame(generation_fitnesses, columns=['Generation', 'Max Fitness', 'Avg Fitness'])
plt.plot(fitness_df['Generation'], fitness_df['Max Fitness'], label='Max Fitness')
plt.plot(fitness_df['Generation'], fitness_df['Avg Fitness'], label='Avg Fitness')

print("En iyi birey:", best_individual)
print("En iyi fitness değeri:", best_fitness)

plt.xlabel('Generation')
plt.ylabel('Fitness Value')
plt.title('Fitness Values')
plt.legend()
plt.show()

