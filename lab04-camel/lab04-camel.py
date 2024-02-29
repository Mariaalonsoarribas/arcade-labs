class Room:
    def __init__(self, descripcion="", norte=0, este=0, sur=0, oeste=0):
        self.descripcion = descripcion
        self.norte = norte
        self.este = este
        self.sur = sur
        self.oeste = oeste

def main():
    room_list = []
    room0 = Room("Estas en la cocina. Puedes ir al norte y al este.", 3, 1, None, None)
    room_list.append(room0)
    room1 = Room("Estas en la sala de juegos. Puedes ir al norte, sur u oeste.", 4, None, 2, 0)
    room_list.append(room1)
    room2 = Room("Estas en la sala de torturas. Puedes ir al norte.", 1, None, None, None )
    room_list.append(room2)
    room3 = Room("Estas en el salon. Puedes ir al norte, este o sur.", 6, 4, 0, None)
    room_list.append(room3)
    room4 = Room("Estas en el cine. Puedes ir donde quieras.", 7, 5, 1, 3)
    room_list.append(room4)
    room5 = Room("Estas en la habitación. Puedes ir al oeste.", None, None, None, 4)
    room_list.append(room5)
    room6 = Room("Estas en la piscina. Puedes ir al este o al sur.", None, 7, 3, None)
    room_list.append(room6)
    room7 = Room("Estas en el bosque. Puedes ir al sur o al oeste.", None, None, 4, 6)
    room_list.append(room7)

    current_room = 0

    # Print the entire room_list
    #print(room_list)

    # Print only the first room in the list
    #print(room_list[0])

    # Print the description of the current room
    #print(room_list[current_room].descripcion)

    done = False
    while (not done):

        print()
        print(room_list[current_room].descripcion)
        user_input = input("¿Qué quieres hacer?\n")

        if "norte" in user_input.lower() or "n" in user_input.lower():
            next_room = room_list[current_room].norte
            if next_room is not None:
                current_room = next_room
            else:
                print("No puedes ir al norte.")

        elif "este" in user_input.lower() or "e" in user_input.lower():
            next_room = room_list[current_room].este
            if next_room is not None:
                current_room = next_room
            else:
                print("No puedes ir al este.")

        elif "sur" in user_input.lower() or "s" in user_input.lower():
            next_room = room_list[current_room].sur
            if next_room is not None:
                current_room = next_room
            else:
                print("No puedes ir al sur.")

        elif "oeste" in user_input.lower() or "o" in user_input.lower():
            next_room = room_list[current_room].oeste
            if next_room is not None:
                current_room = next_room
            else:
                print("No puedes ir al oeste.")
        elif "quit" in user_input.lower() or "q" in user_input.lower():
            print("Gracias por jugar! Adios!")
            done = True

        else:
            print("No entiendo lo que has escrito")


if __name__ == "__main__":
    main()