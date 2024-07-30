l = [1, 2, 3, 5, 6, 8, 2, 3, 4, 9, 7, 8]

def find_consecutive_numbers(lst):
    all_consecutive = []
    current_consecutive = []

    for i in range(len(lst)):
        if current_consecutive and lst[i] != current_consecutive[-1] + 1:
            all_consecutive.append(current_consecutive)
            current_consecutive = []
        current_consecutive.append(lst[i])
    
    if current_consecutive:
        all_consecutive.append(current_consecutive)
    
    return all_consecutive

consecutive_sequences = find_consecutive_numbers(l)

for sequence in consecutive_sequences:
    print(sequence)
print("this is consicutive number print program")
print("this is consicutive number print program1")

