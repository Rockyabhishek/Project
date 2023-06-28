import tkinter as tk
import csv


def Send_data():
  cust=entry1.get()
  mobile=entry2.get()
  adress=entry3.get()
  purchased=entry4.get()
  data=["customer name","Mobile","Adress","Purchased Cost"]

  file_name="emp.csv"
  with open(file_name,"a", newline="") as employee_data:
    file=csv.writer(employee_data)
    #file.writer(data)
    file.writerow([cust,mobile,adress,purchased])


    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    print(file_name)
main=tk.Tk()
main.title("Customer Details")
main.geometry("600x600")

label1=tk.Label(main,text="Customer name ",).grid(row=1,column=1)
label1=tk.Label(main,text="Mobile number ",).grid(row=2,column=1)
label1=tk.Label(main,text="Adress",).grid(row=3,column=1)
label1=tk.Label(main,text="Purchased cost",).grid(row=4,column=1)
button1=tk.Button(main,text="Send",command=Send_data)
button1.grid(row=5,column=2)

entry1=tk.Entry(main)
entry1.grid(row=1,column=2)
entry2=tk.Entry(main)
entry2.grid(row=2,column=2)
entry3=tk.Entry(main)
entry3.grid(row=3,column=2)
entry4=tk.Entry(main)
entry4.grid(row=4,column=2)

main.mainloop()


