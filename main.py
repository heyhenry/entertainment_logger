def menu():

    print("--- Menu ---")
    print("1. Update anime")
    print("2. Show anime list")
    print("3. Exit")
    print("--- [  ] ---")
    
    choice = int(input("Enter 1 - 3: "))

    if choice == 2:
        display_anime_list("anime.records")

def display_anime_list(filename : str):

    with open(filename, 'r') as file:
        
        read_content = file.read()

        lines = read_content.splitlines()
        
        # displays the titles
        # categories = []
        # title_bar = ''

        # for i in lines[0].split(','):
        #     categories.append(i)

        # for i in range(len(categories)):
        #     if i != len(categories) - 1:
        #         title_bar += (categories[i] + ' | ')
        #     else:
        #         title_bar += categories[i]

        content = []

        for i in lines:
            line = i.split(',')
            content.append(line)

        for row in content:
            display_line = ''
            for i in range(len(row)):
                if i != len(row) - 1:
                    display_line += (row[i] + ' | ')
                else:
                    display_line += row[i]
            print(display_line)

def main():
    print(menu())
    # print(display_anime_list("anime.records")) # test case

if __name__ == "__main__":
    main()