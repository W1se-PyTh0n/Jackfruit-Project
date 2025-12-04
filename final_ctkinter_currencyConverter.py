import requests
from datetime import datetime, timedelta
import customtkinter as ctk
import matplotlib.pyplot as mplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

exchangeapi_API_KEY = "7797f7705778ec83f05fa22d"
exchangeapi_url = f"https://v6.exchangerate-api.com/v6/{exchangeapi_API_KEY}"
frankfurterapi_url = "https://api.frankfurter.dev/v1"

def get_exchangeapi_codes():
    return requests.get(f"{exchangeapi_url}/codes").json()["supported_codes"]
    # return [code[0] for code in response]

def convert_currency(base_currency, target_currency, amount = 1):
    response = requests.get(f"{exchangeapi_url}/pair/{base_currency}/{target_currency}/{amount}").json()
    if response["result"] == "success":
        return response["conversion_result"]
    else:
        return None

def get_last_7_days(base, target):
    # Return 7-day history for chart using Frankfurter API (SELECT CURRENCIES ONLY)
    end = datetime.now()
    start = end - timedelta(days=7)

    s = start.strftime("%Y-%m-%d")
    e = end.strftime("%Y-%m-%d")

    response = requests.get(f"{frankfurterapi_url}/{s}..{e}?base={base}&symbols={target}").json()

    dates = list(response["rates"].keys())

    if len(dates) < 7:
        difference = len(dates) - 7
        start = end - timedelta(days= 7 - difference)
        s = start.strftime("%Y-%m-%d")
        e = end.strftime("%Y-%m-%d")

        response = requests.get(f"{frankfurterapi_url}/{s}..{e}?base={base}&symbols={target}").json()

        dates = list(response["rates"].keys())

    values = list()
    for date in dates:
        values.append(response["rates"][date][target])

    return dates, values

def get_frankfurter_codes():
    # Get supported currency codes from frankfurter api
    return list(requests.get(f"{frankfurterapi_url}/currencies").json().keys())

def main():
    app = ctk.CTk()

    app.title("Currency Converter")
    app.geometry("800x600")
    ctk.set_default_color_theme("dark-blue")
    ctk.set_appearance_mode("dark")

    # Heading
    heading = ctk.CTkLabel(app, text="💱 Currency Converter", font=("Helvetica", 40, "bold"), text_color="#FFD700")
    heading.pack(pady=10)
 
    # Main frame
    frame = ctk.CTkFrame(app, corner_radius=15, fg_color="#1f1f2e")
    frame.pack(pady=10)

    # Amount input
    amount_label = ctk.CTkLabel(frame, text="Amount:", font=("Helvetica", 20))
    amount_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    amount_input = ctk.CTkEntry(frame, placeholder_text="Enter amount", font=("Helvetica", 18), width=200, corner_radius=8)
    amount_input.grid(row=0, column=1, padx=10, pady=10)

    # Currency codes
    currency_codes = [code[0] for code in get_exchangeapi_codes()]

    # Base currency
    base_label = ctk.CTkLabel(frame, text="From:", font=("Helvetica", 20))
    base_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    base_currency = ctk.CTkComboBox(frame, values=currency_codes, font=("Helvetica", 18), width=150, button_color="#4B0082")
    base_currency.grid(row=1, column=1, padx=10, pady=10)
    base_currency.set("USD")

    # Target currency
    target_label = ctk.CTkLabel(frame, text="To:", font=("Helvetica", 20))
    target_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    target_currency = ctk.CTkComboBox(frame, values=currency_codes, font=("Helvetica", 18), width=150, button_color="#4B0082")
    target_currency.grid(row=2, column=1, padx=10, pady=10)
    target_currency.set("INR")

    result_label = ctk.CTkLabel(app, text="", font=("Helvetica", 26, "bold"), text_color="#00FFFF")
    result_label.pack(pady=10)

    # Conversion function
    def do_convert():
        base = base_currency.get()
        target = target_currency.get()
        amount = amount_input.get()

        # Validate input
        if not amount or not amount.replace(".", "", 1).isdigit():
            popup = ctk.CTkToplevel(app)
            popup.grab_set()
            popup.lift()

            popup.title("Error")
            popup.geometry("300x150")   

            popup_label = ctk.CTkLabel(popup, text="Please enter a valid number", font=("Helvetica", 14), text_color="#FF4500")
            popup_label.pack(pady=20)

            popup_close_btn = ctk.CTkButton(popup, text="Close", command=popup.destroy, fg_color="#FF4500", hover_color="#FF6347")
            popup_close_btn.pack(pady=10)
            
            return 
        
        elif not base in currency_codes or not target in currency_codes:
            popup = ctk.CTkToplevel(app)
            popup.grab_set()
            popup.lift()

            popup.title("Error")
            popup.geometry("300x150")

            popup_label = ctk.CTkLabel(popup, text="Please enter a valid Currency", font=("Helvetica", 14), text_color="#FF4500")
            popup_label.pack(pady=20)

            popup_close_btn = ctk.CTkButton(popup, text="Close", command=popup.destroy, fg_color="#FF4500", hover_color="#FF6347")
            popup_close_btn.pack(pady=10)
            
            return 
        
        amount = float(amount)
        conv_amount = convert_currency(base, target, amount)
        result_label.configure(text=f"{amount} {base} = {conv_amount} {target}")

    # Convert button
    convert_btn = ctk.CTkButton(frame, text="Convert", command=do_convert, font=("Helvetica", 18), fg_color="#4B0082", hover_color="#6A0DAD")
    convert_btn.grid(row=3, column=0, columnspan=2, pady=15)

    def exapi_currencies():
        currList = ctk.CTkToplevel(app)

        currList.title("Supported Currencies")
        currList.geometry("450x400")
        currList.lift()

        textbox = ctk.CTkTextbox(currList, width=400, height=300, font=("Helvetica", 14), corner_radius=10)
        textbox.pack(pady= 10)

        for code, currency in get_exchangeapi_codes():
            textbox.insert("end", f"{code} - {currency}\n")

        textbox.configure(state="disabled")

        ctk.CTkButton(currList, text="Close", command=currList.destroy, fg_color="#4B0082", hover_color="#6A0DAD", font=("Helvetica", 16)).pack(pady=10)

        return
    
    show_exchangeapi_codes = ctk.CTkButton(app, text="Currency Codes",  )
    show_exchangeapi_codes.pack(pady= 10)

    def seven_day_chart():
        chart_win = ctk.CTkToplevel(app)
        chart_win.title("📈7-day currency comparison chart (ONLY CURRENCIES SUPPORTED BY FRANKFURTER API)")
        chart_win.grab_set()
        chart_win.geometry("900x720")

        base_l = ctk.CTkLabel(chart_win, text="Base Currency: ", font=("Helvetica", 16)).pack(pady= 5)
        base_curr = ctk.CTkComboBox(chart_win, values=get_frankfurter_codes(), font=("Helvetica", 16), width=150, button_color="#4B0082")
        base_curr.set("USD")
        base_curr.pack(pady= 5)

        target_l = ctk.CTkLabel(chart_win, text="Target Currency: ", font=("Helvetica", 16)).pack(pady= 5)
        target_curr = ctk.CTkComboBox(chart_win, values=get_frankfurter_codes(), font=("Helvetica", 16), width=150, button_color="#4B0082")
        target_curr.set("INR")
        target_curr.pack(pady= 5)

        fig, ax = mplot.subplots()
        chart = FigureCanvasTkAgg(fig, master=chart_win)
        chart_widget = chart.get_tk_widget()
        chart_widget.pack(pady=10)
        
        def do_chart():
            base = base_curr.get()
            target = target_curr.get()

            if not base in get_frankfurter_codes() or not target in get_frankfurter_codes():
                popup = ctk.CTkToplevel(app)
                popup.grab_set()
                popup.lift()

                popup.title("Error")
                popup.geometry("250x100")

                popup_label = ctk.CTkLabel(popup, text="Please enter a valid Currency Code", font=("Helvetica", 14), text_color="#FF4500")
                popup_label.pack(pady=20)

                popup_close_btn = ctk.CTkButton(popup, text="Close", command=popup.destroy, fg_color="#FF4500", hover_color="#FF6347", font=("Helvetica", 12))
                popup_close_btn.pack(pady=10)
            
                return 
                
            dates, values = get_last_7_days(base, target)

            clean_dates = list()
            for date in dates:
                date = date.split("-")
                clean_dates.append(f"{date[2]}-{date[1]}")
            
            ax.clear()
            ax.plot(clean_dates, values, marker="o", color="#00FFFF")
            ax.set_title(f"1 {base} --> {target} (Last 7 days)", fontsize=16, color="#000000")
            ax.set_xlabel("Dates", fontsize=12, color="#000000")
            ax.set_ylabel("Exchange Rate", fontsize=12, color="#000000")
            ax.grid(True)
            fig.tight_layout()

            chart.draw()
            chart_widget.update_idletasks()
        
        ctk.CTkButton(chart_win, text="Show Chart", command=do_chart, font=("Helvetica", 16), fg_color="#4B0082", hover_color="#6A0DAD").pack(pady=10)
        ctk.CTkButton(chart_win, text="Close", command=chart_win.destroy, font=("Helvetica", 16), fg_color="#FF4500", hover_color="#FF6347").pack(pady=10)
    
    chart_btn = ctk.CTkButton(app, text="7-day Currency Comparison", font=("Helvetica", 18), fg_color="#4B0082", hover_color="#6A0DAD", command=seven_day_chart)
    chart_btn.pack(pady = 15)

    app.mainloop()

if __name__ == '__main__':

    main()
