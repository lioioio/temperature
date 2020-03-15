import cmd
import storage
import json
from pprint import pprint

days = {'mon': 1 , 'tue': 2, 'etc...': 'etc...'}


error_message = "Ошибка задания аргументов" #сообщение об ошибке, могут быть разными


def is_day(args):
    return args in "1234567" and int(args) < 8 and int(args) > 0

class Cli(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '> '
        self.intro = "Приветствие" 
        self.doc_header = "Доступные команды 'help _команда_'"

    def do_get_schedule(self, args):
        """Метод выводит расписание на неделю
            или на определенный день недели 
        """
        if args == '':
            # Если аргументы не заданы 
            print(storage.get_schedule())
        elif is_day(args):
            # Если задан день недели
            print(storage.get_schedule(args))
        else:
            print(error_message)

    def do_change_schedule(self, args):
        """
            Метод задает расписание  на определенный
            1 {"1": "Математика"}
        """
        args = args.split()
        if len(args) > 1:
            day = args[0]
            schedule = ''.join(args[1:])
            if is_day(day):
                print(schedule)
                try:
                    storage.change_schedule(day, json.loads(schedule))
                except Exception:
                    print(error_message)
            else:
                print(error_message)
        else:
            print(error_message)

    def do_add_note(self, args):
        """
            Добавления методов
                день
                событие
                текст 
        """
        args = args.split()
        if len(args) > 2:
            day = args[0]

            if is_day(day):
                event = args[1]
                note = ''.join(args[2:])
                storage.add_note(day, event, note)
                print("Заметка добавлена")
            else:
                print(error_message)
        else:
            print(error_message)

    def do_add_todo(self, args):
        """
            Добавления методов
                день
                событие
                текст 
        """
        if len(args.split()) > 2:
            day = args.split()[0]
            event = args.split()[1]
            note = ''.join(args.split()[2:])

            if is_day(day):
                storage.add_note(day, event, note, todo=True)
            else:
                print(error_message)
        else:
            print(error_message)

    def do_mark_as_done(self, args):
        """
            ргументы
                день
                событие
                номер заметки
        """
        if len(args.split()) == 3:

            day = args.split()[0]
            if is_day(day):

                event = args.split()[1]
                note_num = args.split()[2]
                storage.done(day, event, note_num)
        else:
            print(error_message)

    def do_get_note(self, args):
        """Выводит заметку
            аргументы
                день
                событие
                номер заметки
        """

        if len(args.split()) == 3:
            day = args.split()[0]
            event = args.split()[1]
            note_num = args.split()[2]
            if is_day(day):
                print(storage.get_notes(day, event).get(note_num, "Заметка отсутствует"))
            else:
                print(error_message)
        else:
            print(error_message)

    def do_exit(self, args):
        """Выход"""
        exit()

    def do_q(self, args):
        """Выход"""
        exit()

    def default(self, line):
        print(error_message)

    def do_show_storage(self, args):
        """Показывает содержимое хранилища"""
        pprint(storage.storage)

if __name__ == "__main__":
    cli = Cli()
    try:
        cli.cmdloop()
    except KeyboardInterrupt:
        exit()

