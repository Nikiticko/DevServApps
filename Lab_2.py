class Tax:
    R = {
        "NDFL": 0.13,
        "SALARY_FREE": 10000,
        "PROPERTY_FREE": 250000,
        "CHILD": 1400,
        "AID_CAP": 4000,
    }

    def __init__(self, name, kind, amount, months=1):
        self.name = name
        self.kind = kind
        self.amount = amount
        self.months = months

    def calc(self):
        if self.kind == "salary":
            base = max(0, self.amount - self.R["SALARY_FREE"] * self.months)
            return round(base * self.R["NDFL"], 2)
        if self.kind in ("side", "royalty", "foreign"):
            return round(self.amount * self.R["NDFL"], 2)
        if self.kind == "property":
            base = max(0, self.amount - self.R["PROPERTY_FREE"])
            return round(base * self.R["NDFL"], 2)
        if self.kind == "aid":
            return -min(self.amount, self.R["AID_CAP"])
        if self.kind == "child":
            return -self.amount * self.R["CHILD"]
        return 0.0

    def __str__(self):
        return f"{self.kind} | {self.name} | {self.amount} → {self.calc()}"


class SalaryTax(Tax):
    def __init__(self, name, amount, months=1):
        super().__init__(name, "salary", amount, months)

    def calc(self):
        base = max(0, self.amount - self.R["SALARY_FREE"] * self.months)
        base = base / 2  
        return round(base * self.R["NDFL"], 2)


def demo():
    return [
        SalaryTax("Зарплата", 120000, months=12), 
        Tax("Фриланс", "side", 18000),
        Tax("Ноутбук", "property", 90000),
        Tax("Авто", "property", 600000),
        Tax("Матпомощь", "aid", 100),
        Tax("Дети", "child", 2),
    ]


def main():
    import os
    items = demo()
    while True:
        os.system("cls")

        print("\nМеню:")
        print("1. Все записи")
        print("2. Итоговый налог")
        print("3. Сортировать по налогу")
        print("4. Поиск по диапазону")
        print("5. Выход")
        cmd = input("> ")

        if cmd == "1":
            for i in items: print(i)
        elif cmd == "2":
            print("ИТОГО:", sum(i.calc() for i in items))
        elif cmd == "3":
            n = len(items)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if items[j].calc() < items[j + 1].calc():
                        items[j], items[j + 1] = items[j + 1], items[j]
            print("Сортировка выполнена.")
        elif cmd == "4":
            low = float(input("min: "))
            high = float(input("max: "))
            for i in items:
                if low <= i.calc() <= high:
                    print(i)
        elif cmd == "5":
            break
        else:
            print("Нет такого пункта.")

        input("\nEnter to exit")


if __name__ == "__main__":
    main()
