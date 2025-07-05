import customtkinter as ctk

def calc_component2_amount():
    try:
        salt1_input = salta.get()
        numbers = [float(x.strip()) for x in salt1_input.split(' ') if x.strip()]
        avg_salt1 = sum(numbers) / len(numbers)
        average.set(f"{avg_salt1:.2f}")

        salt2 = float(corrector.get())
        salt_target = float(desired.get())
        amount1 = float(batchsize.get())

        # Quotient számítás
        quotient1 = (salt_target - salt2) / (avg_salt1 - salt2)
        quotient2 = 1 - quotient1

        amount2 = amount1 * (quotient2 / quotient1)
        componentqty.set(f"{amount2:.2f}")
        newqty.set(f"{amount2 + amount1:.2f}")

    except Exception as e:
        average.set("Error!")
        componentqty.set("Error!")
        newqty.set("Error!")
        print("Error:", e)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

win = ctk.CTk()
win.geometry("550x200")
win.title("SALT CORRECTOR")
win.resizable(False, False)

salta = ctk.CTkEntry(master=win, placeholder_text="                     %", width=160, corner_radius=9)
salta.grid(row=1, column=2, padx=10, pady=10)
ctk.CTkLabel(win, text="MEASURED SALT:", text_color="red",font=("Helvetica", 14)).grid(row=1, column=1)

average = ctk.StringVar()

ctk.CTkLabel(win, textvariable=average, font=("Helvetica", 14), width=110,corner_radius=9, fg_color="yellow", text_color="black").place(x=410, y=10)
ctk.CTkLabel(win, text="AVERAGE:", text_color="red",font=("Helvetica", 14)).place(x=330, y=10)

batchsize = ctk.CTkEntry(master=win, placeholder_text="                    KG", width=160, corner_radius=9)
batchsize.grid(row=2, column=2, padx=10, pady=10)
ctk.CTkLabel(win, text="BATCH SIZE:", text_color="red",font=("Helvetica", 14)).grid(row=2, column=1)

desired = ctk.CTkEntry(master=win, placeholder_text="                     %", width=160, corner_radius=9)
desired.grid(row=3, column=2, padx=10, pady=10)
ctk.CTkLabel(win, text="TARGET SALT:", text_color="red",font=("Helvetica", 14)).grid(row=3, column=1)

corrector = ctk.CTkEntry(master=win, placeholder_text="                     %", width=160, corner_radius=9)
corrector.grid(row=4, column=2, padx=10, pady=10)
ctk.CTkLabel(win, text="COMPONENT SALT:", text_color="#28fc03",font=("Helvetica", 14)).grid(row=4, column=1,padx=5)


componentqty = ctk.StringVar()
ctk.CTkLabel(win, text="QTY:", font=("Helvetica", 14), text_color="#28fc03").place(x=350, y=155)
ctk.CTkLabel(win, textvariable=componentqty, font=("Helvetica", 14), width=110, corner_radius=9, fg_color="yellow", text_color="black").place(x=410, y=155)

newqty = ctk.StringVar()
ctk.CTkLabel(win, text="NEW SIZE:", font=("Helvetica", 14), text_color="red").place(x=330, y=60)
ctk.CTkLabel(win, textvariable=newqty, font=("Helvetica", 14), width=110, corner_radius=9, fg_color="yellow", text_color="black").place(x=410, y=60)

calculate_button = ctk.CTkButton(win, text="Calculate", command=calc_component2_amount, fg_color="red", hover_color="yellow" , text_color="black", width = 110, corner_radius=9)
calculate_button.place(x=410, y=106)

win.mainloop()
