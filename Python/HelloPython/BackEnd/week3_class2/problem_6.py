class ContactList(list):
    def search_by_name(self,*name):
        self.sovpadenie = []
        self.all_contacts = ["Карылгач","Ули","кайрат","Азат","баран","Айдай",
        "Асылбек","Нурс","Альбина","Мырзайым","Олехан","Али","Адил","Байэл"]
        for i in name:
            if i in self.all_contacts:
                self.sovpadenie.append(i)
                print(f"Совпал контакт {i}!")

            elif i not in self.all_contacts:
                print(f"Совпадений {i} не найдено!")

        print(f"Список всех совпадений {self.sovpadenie}")

s = ContactList()
s.search_by_name("Бакыт","Бая","Элянора","Байэл","Али","Айдай")

