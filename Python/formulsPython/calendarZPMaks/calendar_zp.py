import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import calendar as cal
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Глобальная переменная для канваса
canvas = None


# Функция для создания календаря с разными цветами для свободных и не свободных дней
def create_corrected_calendar(year, month, free_days, not_free_days):
    # Массив дней недели
    days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    # Получаем календарь месяца
    month_days = cal.monthcalendar(year, month)

    # Создаем фигуру для отображения
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xticks(np.arange(7))  # 7 дней недели
    ax.set_yticks(np.arange(6))  # Максимум 6 строк для дней месяца (некоторые месяцы могут не иметь всех 6 строк)

    # Отображаем дни недели
    ax.set_xticklabels(days)

    # Оставляем пустые значения для дни месяца, которые выходят за пределы текущего месяца
    ax.set_yticklabels([])

    for week_idx, week in enumerate(month_days):
        for day_idx, day in enumerate(week):
            if day != 0:  # Пропускаем нули (дни, которые выходят за пределы месяца)
                # Проверяем, является ли день свободным
                if day in free_days:
                    ax.text(day_idx, week_idx, str(day), ha='center', va='center', color="white", fontsize=12,
                            fontweight='bold', bbox=dict(facecolor='green', edgecolor='none', boxstyle='round,pad=0.5'))
                # Проверяем, является ли день не свободным
                elif day in not_free_days:
                    ax.text(day_idx, week_idx, str(day), ha='center', va='center', color="white", fontsize=12,
                            fontweight='bold', bbox=dict(facecolor='red', edgecolor='none', boxstyle='round,pad=0.5'))
                else:
                    ax.text(day_idx, week_idx, str(day), ha='center', va='center', fontsize=12)

    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-0.5, 5.5)  # Всего 6 строк (недели)
    ax.invert_yaxis()  # Переворачиваем ось Y для корректного отображения дней сверху вниз
    plt.title(f"Календарь {cal.month_name[month]} {year}")
    plt.tight_layout()

    return fig, ax


# Функция для подсчета рабочих дней и расчета общей суммы
def calculate_working_days(not_free_days):
    working_days = len(not_free_days)
    total_amount = working_days * 1800
    return working_days, total_amount


# Функция для обновления календаря и отображения суммы
def update_calendar(month, free_days, not_free_days, label, working_label, not_working_label):
    global canvas  # Указываем, что работаем с глобальной переменной
    fig, ax = create_corrected_calendar(2024, month, free_days, not_free_days)

    if canvas:  # Если канвас уже создан, удаляем старый
        canvas.get_tk_widget().destroy()

    # Создаем новый канвас
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().grid(row=0, column=0)
    canvas.draw()

    # Подсчитываем и отображаем сумму и количество рабочих/нерабочих дней
    working_days, total_amount = calculate_working_days(not_free_days)
    not_working_days = len(free_days)

    label.config(text=f"Общая сумма: {total_amount} СОМ")
    working_label.config(text=f"Рабочих дней: {working_days}")
    not_working_label.config(text=f"Нерабочих дней: {not_working_days}")


# Настройка интерфейса с Tkinter
root = tk.Tk()
root.title("Календарь 2024")
frame = ttk.Frame(root)
frame.grid(row=0, column=0)

# Добавление меток для отображения суммы и количества дней
total_label = ttk.Label(root, text="Общая сумма: 0 COM", font=("Arial", 12))
total_label.grid(row=6, column=0)

working_label = ttk.Label(root, text="Рабочих дней: 0", font=("Arial", 12))
working_label.grid(row=7, column=0)

not_working_label = ttk.Label(root, text="Нерабочих дней: 0", font=("Arial", 12))
not_working_label.grid(row=8, column=0)

# Дни, когда ты свободен
free_days_november = [20, 21, 23, 24, 26, 27, 29, 30]
not_free_days_november = [19, 22, 25, 28]

free_days_december = [2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30]
not_free_days_december = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31]

free_days_january = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29, 31]
not_free_days_january = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

free_days_february = [1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 22, 24, 25, 27, 28]
not_free_days_february = [2, 5, 8, 11, 14, 17, 20, 23, 26]

free_days_march = [2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30]
not_free_days_march = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31]

# Добавление календаря для Ноября
fig, ax = create_corrected_calendar(2024, 11, free_days_november, not_free_days_november)  # Ноябрь по умолчанию
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().grid(row=0, column=0)


# Кнопки для переключения месяцев
def show_november():
    update_calendar(11, free_days_november, not_free_days_november, total_label, working_label,
                    not_working_label)  # Ноябрь


def show_december():
    update_calendar(12, free_days_december, not_free_days_december, total_label, working_label,
                    not_working_label)  # Декабрь


def show_january():
    update_calendar(1, free_days_january, not_free_days_january, total_label, working_label,
                    not_working_label)  # Январь


def show_february():
    update_calendar(2, free_days_february, not_free_days_february, total_label, working_label,
                    not_working_label)  # Февраль


def show_march():
    update_calendar(3, free_days_march, not_free_days_march, total_label, working_label, not_working_label)  # Март


november_button = ttk.Button(root, text="Ноябрь", command=show_november)
november_button.grid(row=1, column=0)

december_button = ttk.Button(root, text="Декабрь", command=show_december)
december_button.grid(row=2, column=0)

january_button = ttk.Button(root, text="Январь", command=show_january)
january_button.grid(row=3, column=0)

february_button = ttk.Button(root, text="Февраль", command=show_february)
february_button.grid(row=4, column=0)

march_button = ttk.Button(root, text="Март", command=show_march)
march_button.grid(row=5, column=0)


# Завершаем работу Tkinter корректно
def on_close():
    root.quit()  # Завершаем работу приложения при закрытии


root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
