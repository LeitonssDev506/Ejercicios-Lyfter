

notes = int(input("Enter the number of notes: "))

total_aproved_notes = 0
total_desaproved_notes = 0
total_notes = 0

notes_aproved = []
notes_desaproved = []

n = 0
while n < notes:
    note = float(input("Enter the note: "))
    total_notes += 1
    n += 1

    if note >= 70:
        total_aproved_notes += 1
        notes_aproved.append(note)
    else:
        total_desaproved_notes += 1
        notes_desaproved.append(note)



print("Total approved notes: ", total_aproved_notes)
print("Total disapproved notes: ", total_desaproved_notes)

if total_aproved_notes > 0:
    print("Average of approved notes: ", sum(notes_aproved) / total_aproved_notes)

else:
    print("No approved notes to calculate average.")

if total_desaproved_notes > 0:
    print("Average of disapproved notes: ", sum(notes_desaproved) / total_desaproved_notes)
else:
    print("No disapproved notes to calculate average.")

#calcula el promedio de las notas totales

total_average_note = (sum(notes_aproved) + sum(notes_desaproved)) / total_notes 

print("Average result of total notes: ", total_average_note)