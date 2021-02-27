

def print_menu() -> None:
    '''prints out menu'''
    print('1. Add Project')
    print('2. Print Shopping List')
    print('3. Quit')


def get_project_id(proj_name_list:list, proj_name:str) -> int:
    '''Returns the index of the given project name'''
    for i, project in enumerate(proj_name_list):
        if project == proj_name:
            return i
    return 100

assert get_project_id(['fancy', 'baby'], 'baby') == 1

def save_shopping_list(project: str, material_list:list,
                       amount_list: list) -> None:
    ''' output shopping list to a file'''
    # with open('shoppingList.txt', 'w') as shopping_list:
    #     shopping_list.write(project)
    #     for material, amount in material_list, amount_list:
    #         shopping_list.write(f'{material} .... {amount}')
    with open('shoppingList.txt', 'w') as shopping_list:
        shopping_list.write(project + '\n\n')
        for i in range(len(material_list)):
            shopping_list.write(f'{material_list[i]} .... {amount_list[i]}\n')

    # print(project)
    # for material, amount in material_list, amount_list:
    #     print(f'{material} .... {amount}')

    # # test output
    # for i in range(len(material_list)):
    #     print(f'{material_list[i]} .... {amount_list[i]}')


def get_materials() -> list:
    ''':return material list from user input'''
    material_list = []
    material = input('Enter the material needed ("quit" to end):  ')
    while material.lower() != 'quit':
        material_list.append(material)
        material = input('Enter the material needed:  ')

    return material_list


def get_amounts(material_list: list) -> list:
    ''':return material amount list correponding to material list from user input'''
    amount_list = []
    for material in material_list:
        amount = int(input('What quantity of yarn do you need?  '))
        amount_list.append(amount)

    return amount_list

def add_project(project_name:list, material_list_list:list,
                amount_list_list:list) -> None:
    '''update new project to the list with name, material list, amount list'''
    name = input('Enter project name: ')
    project_name.append(name)
    material = get_materials()
    material_list_list.append(material)
    amount = get_amounts(material)
    amount_list_list.append(amount)


def main() -> None:
    project_names = ["Fancy Table", "Baby Blanket"]
    materials = [["wood", "nails", "wood glue"],
                 ["yarn", "stitch markers", "knitting needles"],
                 ]
    amounts = [[10, 53, 2],
               [3, 20, 4]
               ]
    print_menu()
    choice = int(input('Enter your choice: '))
    if choice == 1:
        add_project(project_names, materials, amounts)
        print(project_names)
    elif choice == 2:
        name = input('Enter querying project name: ')
        idx = get_project_id(project_names, name)
        save_shopping_list(name, materials[idx], amounts[idx])
    else:
        print('There is no such choice.')

if __name__ == '__main__':
    main()
