#!/usr/bin/env python3
"""This module houses the HBNB class definition
and its attributes and methods"""

import cmd
import sys
import os

sys.path.append(os.getcwd())
try:
    from models.base_model import BaseModel
    from models.user import User
    from models import storage
    from models.amenity import Amenity
    from models.city import City
    from models.place import Place
    from models.review import Review
    from models.state import State
except Exception as e:
    print(e)


class HBNBCommand(cmd.Cmd):
    """This class houses the configuration of the line-oriented
    interpreter interface for the AirBNB project"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """This is a quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """This method closes or terminates this session"""
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """This method creates a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
        elif (line != "BaseModel" and line != "User" and line != "Amenity" and
              line != "City" and line != "Place" and line != "Review" and
              line != "State"):
            print("** class doesn't exist **")
        else:
            if line == "BaseModel":
                b = BaseModel()
                b.name = "ALX"
                b.save()
                print(b.id)
            elif line == "User":
                u = User()
                u.first_name = "ALX"
                u.last_name = "Nigeria"
                u.email = "info@alxswe.com"
                u.password = "root"
                u.save()
                print(u.id)
            elif line == "Amenity":
                am = Amenity()
                am.name = "Rooftop"
                am.save()
                print(am.id)
            elif line == "City":
                c = City()
                c.state_id = "State ID"
                c.name = "Lagos"
                c.save()
                print(c.id)
            elif line == "Place":
                pl = Place()
                pl.city_id = "City ID"
                pl.user_id = "User ID"
                pl.name = "Ikeja"
                pl.description = "A Bugalow with a rooftop"
                pl.number_rooms = 3
                pl.number_bathrooms = 3
                pl.max_guest = 9
                pl.price_per_night = 150
                pl.latitude = 07777.888
                pl.longitude = 9222.134
                pl.amenity_ids = [12333]
                pl.save()
                print(pl.id)
            elif line == "Review":
                r = Review()
                r.place_id = "Place ID"
                r.user_id = "User ID"
                r.text = "A very nice place"
                r.save()
                print(r.id)
            elif line == "State":
                st = State()
                st.name = "Lagos"
                st.save()
                print(st.id)

    def do_show(self, line):
        """This method shows the instance details
        of the given id

        Args:
            line - the argument to the command
        """
        if not line:
            print("** class name missing **")
        else:
            data = line.split()
            if (
               data[0] != 'BaseModel' and data[0] != 'User' and
               data[0] != 'Amenity' and data[0] != 'City' and
               data[0] != 'Place' and data[0] != 'Review' and
               data[0] != 'State'
               ):
                print("** class doesn't exist **")
            elif len(data) != 2:
                print("** instance id missing **")
            else:
                fs = storage
                all_objs = fs.all()
                bk = f'BaseModel.{data[1]}' not in all_objs.keys()
                uk = f'User.{data[1]}' not in all_objs.keys()
                ak = f'Amenity.{data[1]}' not in all_objs.keys()
                ck = f'City.{data[1]}' not in all_objs.keys()
                pk = f'Place.{data[1]}' not in all_objs.keys()
                rk = f'Review.{data[1]}' not in all_objs.keys()
                sk = f'State.{data[1]}' not in all_objs.keys()
                if bk and uk and ak and ck and pk and rk and sk:
                    print("** no instance found **")
                else:
                    for key in all_objs.keys():
                        if f'BaseModel.{data[1]}' == key:
                            b = BaseModel(**all_objs[key])
                            print(b)
                        elif f'User.{data[1]}' == key:
                            u = User(**all_objs[key])
                            print(u)
                        elif f'City.{data[1]}' == key:
                            c = City(**all_objs[key])
                            print(c)
                        elif f'Place.{data[1]}' == key:
                            p = Place(**all_objs[key])
                            print(p)
                        elif f'Amenity.{data[1]}' == key:
                            a = Amenity(**all_objs[key])
                            print(a)
                        elif f'Review.{data[1]}' == key:
                            r = Review(**all_objs[key])
                            print(r)
                        elif f'State.{data[1]}' == key:
                            s = State(**all_objs[key])
                            print(s)

    def do_destroy(self, line):
        """This method deletes an instance based on
        the class name and id

        Args:
            line - the command argument, passed.
        """
        if not line:
            print("** class name missing **")
        else:
            data = line.split()
            if (
               data[0] != 'BaseModel' and data[0] != 'User' and
               data[0] != 'Amenity' and data[0] != 'City' and
               data[0] != 'Place' and data[0] != 'Review' and
               data[0] != 'State'
               ):
                print("** class doesn't exist **")
            elif len(data) < 2:
                print("** instance id missing **")
            else:
                fs = storage
                all_objs = fs.all()
                keys = [
                        f'BaseModel.{data[1]}',
                        f'User.{data[1]}',
                        f'Amenity.{data[1]}',
                        f'City.{data[1]}',
                        f'Place.{data[1]}',
                        f'Review.{data[1]}',
                        f'State.{data[1]}'
                       ]
                no_k0 = keys[0] not in all_objs.keys()
                no_k1 = keys[1] not in all_objs.keys()
                no_k2 = keys[2] not in all_objs.keys()
                no_k3 = keys[3] not in all_objs.keys()
                no_k4 = keys[4] not in all_objs.keys()
                no_k5 = keys[5] not in all_objs.keys()
                no_k6 = keys[6] not in all_objs.keys()
                if (
                   no_k0 and no_k1 and no_k2 and no_k3 and
                   no_k4 and no_k5 and no_k6
                   ):
                    print("** no instance found **")
                else:
                    for k in all_objs.keys():
                        if (
                           (k == keys[0]) or (k == keys[1]) or
                           (k == keys[2]) or (k == keys[3]) or
                           (k == keys[4]) or (k == keys[5]) or
                           (k == keys[6])
                           ):
                            all_objs.pop(k)
                            break
                    for obj_key in all_objs.keys():
                        if 'BaseModel' in obj_key:
                            o = BaseModel(**all_objs[obj_key])
                            fs.new(o)
                        elif 'User' in obj_key:
                            o = User(**all_objs[obj_key])
                            fs.new(o)
                        elif 'Amenity' in obj_key:
                            o = Amenity(**all_objs[obj_key])
                            fs.new(o)
                        elif 'City' in obj_key:
                            o = City(**all_objs[obj_key])
                            fs.new(o)
                        elif 'Place' in obj_key:
                            o = Place(**all_objs[obj_key])
                            fs.new(o)
                        elif 'Review' in obj_key:
                            o = Review(**all_objs[obj_key])
                            fs.new(o)
                        elif 'State' in obj_key:
                            o = State(**all_objs[obj_key])
                            fs.new(o)
                    fs.save()

    def do_all(self, line):
        """This method prints all string representation
        of all instances based or not on the class name

        Args:
           line - the command argument, passed.
        """
        if (
           line and line != 'BaseModel' and line != 'User' and
           line != "City" and line != "Place" and line != 'Amenity' and
           line != "Review" and line != "State"
           ):
            print("** class doesn't exist **")
        else:
            data = []
            fs = storage
            all_objs = fs.all()
            if not line:
                for key in all_objs.keys():
                    if 'User' in key:
                        temp = User(**all_objs[key])
                    elif 'BaseModel' in key:
                        temp = BaseModel(**all_objs[key])
                    elif 'Amenity' in key:
                        temp = Amenity(**all_objs[key])
                    elif 'City' in key:
                        temp = CIty(**all_objs[key])
                    elif 'Place' in key:
                        temp = Place(**all_objs[key])
                    elif 'Review' in key:
                        temp = Review(**all_objs[key])
                    elif 'State' in key:
                        temp = State(**all_objs[key])
                    data.append(str(temp))
            elif line == 'User':
                for key in all_objs.keys():
                    if 'User' in key:
                        temp = User(**all_objs[key])
                        data.append(str(temp))
            elif line == 'BaseModel':
                for key in all_objs.keys():
                    if 'BaseModel' in key:
                        temp = BaseModel(**all_objs[key])
                        data.append(str(temp))
            elif line == 'Amenity':
                for key in all_objs.keys():
                    if 'Amenity' in key:
                        temp = Amenity(**all_objs[key])
                        data.append(str(temp))
            elif line == 'City':
                for key in all_objs.keys():
                    if 'City' in key:
                        temp = City(**all_objs[key])
                        data.append(str(temp))
            elif line == 'Place':
                for key in all_objs.keys():
                    if 'Place' in key:
                        temp = Place(**all_objs[key])
                        data.append(str(temp))
            elif line == 'Review':
                for key in all_objs.keys():
                    if 'Review' in key:
                        temp = Review(**all_objs[key])
                        data.append(str(temp))
            elif line == 'State':
                for key in all_objs.keys():
                    if 'State' in key:
                        temp = State(**all_objs[key])
                        data.append(str(temp))
            print(data)

    def do_update(self, line):
        """This method updates an instance based on the class
        name and id by adding or updating attribute (save the
        change into the JSON file).

        Args:
            line - the command line argurment(s)
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if (
               args[0] != 'BaseModel' and args[0] != 'User' and
               args[0] != 'Amenity' and args[0] != 'City' and
               args[0] != 'Place' and args[0] != 'Review' and
               args[0] != 'State'
               ):
                print("** class doesn't exist **")
            elif not args[1]:
                print("** instance id missing **")
            else:
                fs = storage
                all_objs = fs.all()
                keys = [
                        f'BaseModel.{args[1]}',
                        f'User.{args[1]}',
                        f'City.{args[1]}',
                        f'Amenity.{args[1]}',
                        f'Place.{args[1]}',
                        f'Review.{args[1]}',
                        f'State.{args[1]}'
                       ]
                no_k0 = keys[0] not in all_objs.keys()
                no_k1 = keys[1] not in all_objs.keys()
                no_k2 = keys[2] not in all_objs.keys()
                no_k3 = keys[3] not in all_objs.keys()
                no_k4 = keys[4] not in all_objs.keys()
                no_k5 = keys[5] not in all_objs.keys()
                no_k6 = keys[6] not in all_objs.keys()
                if (
                   no_k0 and no_k1 and no_k2 and no_k3 and
                   no_k4 and no_k5 and no_k6
                   ):
                    print("** no instance found **")
                else:
                    if len(args) < 3:
                        print("** attribute name missing **")
                    elif len(args) < 4:
                        print("** value missing **")
                    else:
                        if args[3].startswith('"'):
                            args[3] = args[3][1:-1]
                            temp = args[3]
                            print(args[3])
                        try:
                            temp = float(args[3])
                            if str(temp) == args[3]:
                                args[3] = temp
                            else:
                                temp = int(args[3])
                                if str(temp) == args[3]:
                                    args[3] = temp
                        except Exception as e:
                            pass
                        for item_dict in all_objs.values():
                            if args[1] == item_dict['id']:
                                item_dict[args[2]] = args[3]
                                if args[0] == 'BaseModel':
                                    o = BaseModel(**item_dict)
                                    fs.new(o)
                                elif args[0] == 'User':
                                    o = User(**item_dict)
                                    fs.new(o)
                                elif args[0] == 'City':
                                    o = City(**item_dict)
                                    fs.new(o)
                                elif args[0] == 'Amenity':
                                    o = Amenity(**item_dict)
                                    fs.new(o)
                                elif args[0] == 'Place':
                                    o = Place(**item_dict)
                                    fs.new(o)
                                elif args[0] == 'Review':
                                    o = Review(**item_dict)
                                    fs.new(o)
                                elif args[0] == 'State':
                                    o = State(**item_dict)
                                    fs.new(o)
                                fs.save()
                                break


if __name__ == '__main__':
    HBNBCommand().cmdloop()
