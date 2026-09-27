


def create_file():
    songs = [
        'Yesterday',
        'Stairway to Heaven',
        "Sweet Child O' Mine",
        'Bohemian Rhapsody',
        'Imagine',
        'Like a Rolling Stone',
        'Smells Like Teen Spirit',
        'Hotel California'
    ]
    for i in range(len(songs)):
        songs[i] = songs[i] + '\n'

    with open('Songs.txt', 'w', encoding='utf-8') as file:
        file.writelines(songs)


path = "Songs.txt"

def bubble_sort_a(songs):

    for i in range(len(songs)):
        songs[i] = songs[i].strip()

    print(songs)

    n = len(songs)
    for i in range(n):
        for j in range(0, n - i - 1):
            
            if songs[j] > songs[j + 1]:
                songs[j], songs[j + 1] = songs[j + 1], songs[j]
    return songs


def read_file_by_lines(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        s = bubble_sort_a(lines)

    return s


def create_file_sorted(s):

    for i in range(len(s)):
            s[i] = s[i] + '\n'
    
    with open('Sorted_songs.txt', 'w', encoding='utf-8') as file:
        file.writelines(s)


def main():
    
    
    create_file()

    songs_sorted = read_file_by_lines(path)

    create_file_sorted(songs_sorted)




if __name__ == '__main__':
	main()




