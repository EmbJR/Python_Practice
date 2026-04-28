import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from tkinter import Frame, Canvas, Scrollbar, Button, Label, Entry, Listbox, Toplevel
import uuid
import time

class IntraTradHelper:
    def __init__(self, root):
        self.root = root
        self.root.title("IntraTradHelper")
        self.root.geometry("1200x600")
        
        # Dictionary to store button names and their associated windows
        self.buttons_dict = {}
        self.window_instances = {}  # Store window instances for each button
        self.button_widgets = {}  # Store button widget references
        self.press_start_time = {}  # Track press start time for each button
        self.button_data = {}  # Store list of dictionaries with price and qty for each button
        
        # Create main container frame
        main_container = Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Left side frame - for displaying button windows
        left_frame = Frame(main_container, bg="lightgray", width=600)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        left_label = Label(left_frame, text="Button Windows", bg="lightgray", font=("Arial", 10, "bold"))
        left_label.pack(pady=5)
        
        self.left_content_frame = Frame(left_frame, bg="white")
        self.left_content_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Right side frame - for scrollable buttons
        right_frame = Frame(main_container, bg="lightyellow", width=300)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False, padx=5)
        
        right_label = Label(right_frame, text="Button Panel", bg="lightyellow", font=("Arial", 10, "bold"))
        right_label.pack(pady=5)
        
        # Create scrollable area
        self.create_scrollable_buttons_area(right_frame)
        
    def create_scrollable_buttons_area(self, parent):
        """Create a scrollable area for buttons"""
        # Create canvas with scrollbar
        canvas = Canvas(parent, bg="lightyellow", highlightthickness=0)
        scrollbar = Scrollbar(parent, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="lightyellow")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Store reference to scrollable frame for adding buttons
        self.scrollable_frame = scrollable_frame
        
        # Bind mousewheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Pack canvas and scrollbar
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Add "+" button at the top to add new buttons
        add_button_frame = Frame(self.scrollable_frame, bg="lightyellow")
        add_button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        add_button = Button(
            add_button_frame,
            text="+",
            font=("Arial", 14, "bold"),
            bg="green",
            fg="white",
            command=self.add_new_button,
            width=15
        )
        add_button.pack(fill=tk.X)
    
    def add_new_button(self):
        """Add a new button to the scrollable area"""
        # Ask user for button name
        dialog = ButtonNameDialog(self.root)
        button_name = dialog.result
        
        if button_name and button_name.strip():
            # Create unique ID for this button
            button_id = str(uuid.uuid4())
            self.buttons_dict[button_id] = button_name
            
            # Create new button
            new_button = Button(
                self.scrollable_frame,
                text=button_name,
                font=("Arial", 10),
                bg="lightblue",
                command=lambda bid=button_id: self.on_button_click(bid),
                height=2
            )
            new_button.pack(fill=tk.X, padx=5, pady=3)
            
            # Store button references
            if button_id not in self.window_instances:
                self.window_instances[button_id] = None
            
            self.button_widgets[button_id] = new_button
            self.press_start_time[button_id] = None
            
            # Bind mouse events for long-press detection
            new_button.bind("<ButtonPress-1>", lambda e, bid=button_id: self.on_button_press(bid, e))
            new_button.bind("<ButtonRelease-1>", lambda e, bid=button_id: self.on_button_release(bid, e))
    
    def on_button_press(self, button_id, event):
        """Record the time when button is pressed"""
        self.press_start_time[button_id] = time.time()
    
    def on_button_release(self, button_id, event):
        """Handle button release - detect long-press or regular click"""
        if self.press_start_time[button_id] is None:
            return
        
        press_duration = time.time() - self.press_start_time[button_id]
        self.press_start_time[button_id] = None
        
        # Long press detected (> 1 second)
        if press_duration > 1.0:
            self.delete_button(button_id)
        # Regular click
        else:
            self.on_button_click(button_id)
    
    def delete_button(self, button_id):
        """Delete a button after confirmation"""
        button_name = self.buttons_dict.get(button_id, "Unknown")
        
        # Show confirmation dialog
        result = messagebox.askyesno(
            "Delete Button",
            f"Are you sure you want to delete the button '{button_name}'?\n\n(Long press to delete)"
        )
        
        if result:
            # Remove from dictionaries
            if button_id in self.buttons_dict:
                del self.buttons_dict[button_id]
            if button_id in self.window_instances:
                del self.window_instances[button_id]
            if button_id in self.button_widgets:
                # Destroy the button widget
                self.button_widgets[button_id].destroy()
                del self.button_widgets[button_id]
            if button_id in self.press_start_time:
                del self.press_start_time[button_id]
            if button_id in self.button_data:
                del self.button_data[button_id]
            
            # Clear left panel if this button's window was displayed
            for widget in self.left_content_frame.winfo_children():
                widget.destroy()
            
            messagebox.showinfo("Success", f"Button '{button_name}' has been deleted.")
    
    def on_button_click(self, button_id):
        """Handle button click - create or show window on left side"""
        button_name = self.buttons_dict.get(button_id, "Unknown")
        
        # Initialize data list for this button if not exists
        if button_id not in self.button_data:
            self.button_data[button_id] = []
        
        # Clear previous content in left frame
        for widget in self.left_content_frame.winfo_children():
            widget.destroy()
        
        # Create new window instance for this button
        window_frame = Frame(self.left_content_frame, bg="white", relief=tk.RAISED, bd=2)
        window_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Add title
        title_label = Label(
            window_frame,
            text=f"Window: {button_name}",
            bg="lightblue",
            font=("Arial", 12, "bold"),
            pady=10
        )
        title_label.pack(fill=tk.X)
        
        # Create main content frame
        content_frame = Frame(window_frame, bg="white")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left side - input area
        input_frame = Frame(content_frame, bg="white")
        input_frame.pack(side=tk.LEFT, anchor="nw", padx=5)
        
        # Price Label and Input
        price_label = Label(input_frame, text="Price:", bg="white", font=("Arial", 10))
        price_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        price_entry = Entry(input_frame, font=("Arial", 10), width=15)
        price_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Qty Label and Input
        qty_label = Label(input_frame, text="Qty:", bg="white", font=("Arial", 10))
        qty_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        qty_entry = Entry(input_frame, font=("Arial", 10), width=15)
        qty_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Current Price Label and Input
        current_price_label = Label(input_frame, text="Current Price:", bg="white", font=("Arial", 10))
        current_price_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        current_price_entry = Entry(input_frame, font=("Arial", 10), width=15)
        current_price_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Total Investment Display (Read-only)
        total_investment_label = Label(input_frame, text="Total Investment:", bg="white", font=("Arial", 10, "bold"))
        total_investment_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        total_investment_value = Entry(input_frame, font=("Arial", 10), width=15, state=tk.DISABLED, disabledbackground="lightyellow", disabledforeground="black")
        total_investment_value.grid(row=3, column=1, padx=5, pady=5)
        
        # Avg Price Display (Read-only)
        avg_price_label = Label(input_frame, text="Avg Price:", bg="white", font=("Arial", 10, "bold"))
        avg_price_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        avg_price_value = Entry(input_frame, font=("Arial", 10), width=15, state=tk.DISABLED, disabledbackground="lightyellow", disabledforeground="black")
        avg_price_value.grid(row=4, column=1, padx=5, pady=5)
        
        # Total Qty Display (Read-only)
        total_qty_label = Label(input_frame, text="Total Qty:", bg="white", font=("Arial", 10, "bold"))
        total_qty_label.grid(row=5, column=0, sticky="w", padx=5, pady=5)
        total_qty_value = Entry(input_frame, font=("Arial", 10), width=15, state=tk.DISABLED, disabledbackground="lightyellow", disabledforeground="black")
        total_qty_value.grid(row=5, column=1, padx=5, pady=5)
        
        # P&L-% Display (Read-only)
        pnl_percent_label = Label(input_frame, text="P&L-%:", bg="white", font=("Arial", 10, "bold"))
        pnl_percent_label.grid(row=6, column=0, sticky="w", padx=5, pady=5)
        pnl_percent_value = Entry(input_frame, font=("Arial", 10), width=15, state=tk.DISABLED, disabledbackground="lightyellow", disabledforeground="black")
        pnl_percent_value.grid(row=6, column=1, padx=5, pady=5)
        
        # P&L_Cash Display (Read-only)
        pnl_cash_label = Label(input_frame, text="P&L_Cash:", bg="white", font=("Arial", 10, "bold"))
        pnl_cash_label.grid(row=7, column=0, sticky="w", padx=5, pady=5)
        pnl_cash_value = Entry(input_frame, font=("Arial", 10), width=15, state=tk.DISABLED, disabledbackground="lightyellow", disabledforeground="black")
        pnl_cash_value.grid(row=7, column=1, padx=5, pady=5)
        
        # Right side - listbox area
        list_frame = Frame(content_frame, bg="white")
        list_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        # Listbox title
        list_title = Label(list_frame, text="Submitted Data", bg="white", font=("Arial", 10, "bold"))
        list_title.pack(pady=5)
        
        # Investment value label
        investment_label = Label(list_frame, text="(Price × Qty)", bg="white", font=("Arial", 8, "italic"))
        investment_label.pack(pady=0)
        
        # Create listbox with scrollbar
        listbox_scroll_frame = Frame(list_frame, bg="white")
        listbox_scroll_frame.pack(fill=tk.BOTH, expand=True)
        
        listbox_scrollbar = Scrollbar(listbox_scroll_frame)
        listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        data_listbox = Listbox(listbox_scroll_frame, font=("Arial", 12, "bold"), yscrollcommand=listbox_scrollbar.set)
        data_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        listbox_scrollbar.config(command=data_listbox.yview)
        
        # Function to calculate and update P&L values
        def update_pnl_values():
            try:
                current_price = float(current_price_entry.get()) if current_price_entry.get() else 0
                avg_price = float(avg_price_value.get()) if avg_price_value.get() else 0
                total_investment = float(total_investment_value.get()) if total_investment_value.get() else 0
                
                # Calculate P&L %
                if avg_price != 0:
                    pnl_percent = ((current_price / avg_price) - 1) * 100
                else:
                    pnl_percent = 0
                
                # Calculate P&L Cash
                pnl_cash = total_investment * (pnl_percent / 100)
                
                # Update P&L % display
                pnl_percent_value.config(state=tk.NORMAL)
                pnl_percent_value.delete(0, tk.END)
                pnl_percent_value.insert(0, str(round(pnl_percent, 2)))
                pnl_percent_value.config(state=tk.DISABLED)
                
                # Update P&L Cash display
                pnl_cash_value.config(state=tk.NORMAL)
                pnl_cash_value.delete(0, tk.END)
                pnl_cash_value.insert(0, str(round(pnl_cash, 2)))
                pnl_cash_value.config(state=tk.DISABLED)
            except (ValueError, ZeroDivisionError):
                pnl_percent_value.config(state=tk.NORMAL)
                pnl_percent_value.delete(0, tk.END)
                pnl_percent_value.config(state=tk.DISABLED)
                
                pnl_cash_value.config(state=tk.NORMAL)
                pnl_cash_value.delete(0, tk.END)
                pnl_cash_value.config(state=tk.DISABLED)
        
        # Display existing data in listbox
        def refresh_listbox():
            data_listbox.delete(0, tk.END)
            total_investment = 0
            total_qty = 0
            for idx, item in enumerate(self.button_data[button_id]):
                investment_value = item['price'] * item['qty']
                total_investment += investment_value
                total_qty += item['qty']
                data_listbox.insert(tk.END, f"{idx+1}> (Price:{item['price']}), (Qty:{item['qty']}), Inv:{investment_value}")
            
            # Calculate average price - Reset to 0 if Total Qty is 0
            # Weighted average: Total Investment / Total Qty
            if total_qty != 0:
                avg_price = total_investment / total_qty
            else:
                avg_price = 0
            
            # Update display boxes
            total_investment_value.config(state=tk.NORMAL)
            total_investment_value.delete(0, tk.END)
            total_investment_value.insert(0, str(total_investment))
            total_investment_value.config(state=tk.DISABLED)
            
            avg_price_value.config(state=tk.NORMAL)
            avg_price_value.delete(0, tk.END)
            avg_price_value.insert(0, str(round(avg_price, 2)))
            avg_price_value.config(state=tk.DISABLED)
            
            total_qty_value.config(state=tk.NORMAL)
            total_qty_value.delete(0, tk.END)
            total_qty_value.insert(0, str(total_qty))
            total_qty_value.config(state=tk.DISABLED)
            
            # Update P&L values after updating all other values
            update_pnl_values()
        
        refresh_listbox()
        
        # Bind Current Price entry to update P&L values on change
        current_price_entry.bind("<KeyRelease>", lambda e: update_pnl_values())
        
        # Submit Button and action buttons frame
        button_frame = Frame(input_frame, bg="white")
        button_frame.grid(row=8, column=0, columnspan=2, padx=5, pady=10)
        
        # Submit Button
        def on_submit():
            try:
                price = float(price_entry.get())
                qty = int(qty_entry.get())
                
                # Add to data dictionary
                self.button_data[button_id].append({
                    "price": price,
                    "qty": qty
                })
                
                # Refresh listbox
                refresh_listbox()
                
                # Clear input fields
                price_entry.delete(0, tk.END)
                qty_entry.delete(0, tk.END)
                current_price_entry.delete(0, tk.END)
                price_entry.focus()
                
                messagebox.showinfo(
                    "Success",
                    f"Price: {price}, Qty: {qty} added successfully!"
                )
            except ValueError:
                messagebox.showerror(
                    "Input Error",
                    "Please enter a valid Price (float) and Qty (integer)"
                )
        
        submit_button = Button(
            button_frame,
            text="Submit",
            font=("Arial", 10),
            bg="green",
            fg="white",
            command=on_submit,
            width=10
        )
        submit_button.pack(side=tk.LEFT, padx=5)
        
        # Edit Button
        def on_edit():
            selection = data_listbox.curselection()
            if not selection:
                messagebox.showwarning("Selection Error", "Please select an entry to edit!")
                return
            
            idx = selection[0]
            item = self.button_data[button_id][idx]
            
            # Create edit dialog
            edit_window = Toplevel(self.root)
            edit_window.title(f"Edit Entry #{idx+1}")
            edit_window.geometry("300x200")
            edit_window.transient(self.root)
            edit_window.grab_set()
            
            # Price field
            Label(edit_window, text="Price:", font=("Arial", 10)).pack(pady=5)
            edit_price = Entry(edit_window, font=("Arial", 10), width=20)
            edit_price.pack(pady=5)
            edit_price.insert(0, str(item['price']))
            
            # Qty field
            Label(edit_window, text="Qty:", font=("Arial", 10)).pack(pady=5)
            edit_qty = Entry(edit_window, font=("Arial", 10), width=20)
            edit_qty.pack(pady=5)
            edit_qty.insert(0, str(item['qty']))
            
            # Save button in edit dialog
            def save_edit():
                try:
                    new_price = float(edit_price.get())
                    new_qty = int(edit_qty.get())
                    
                    self.button_data[button_id][idx] = {
                        "price": new_price,
                        "qty": new_qty
                    }
                    
                    refresh_listbox()
                    edit_window.destroy()
                    messagebox.showinfo("Success", "Entry updated successfully!")
                except ValueError:
                    messagebox.showerror("Input Error", "Invalid Price or Qty values!")
            
            save_button = Button(edit_window, text="Save", command=save_edit, bg="blue", fg="white")
            save_button.pack(pady=10)
        
        edit_button = Button(
            button_frame,
            text="Edit",
            font=("Arial", 10),
            bg="orange",
            fg="white",
            command=on_edit,
            width=10
        )
        edit_button.pack(side=tk.LEFT, padx=5)
        
        # Delete Button
        def on_delete():
            selection = data_listbox.curselection()
            if not selection:
                messagebox.showwarning("Selection Error", "Please select an entry to delete!")
                return
            
            idx = selection[0]
            result = messagebox.askyesno("Confirm Delete", f"Delete entry #{idx+1}?")
            if result:
                del self.button_data[button_id][idx]
                refresh_listbox()
                messagebox.showinfo("Success", "Entry deleted!")
        
        delete_button = Button(
            button_frame,
            text="Delete",
            font=("Arial", 10),
            bg="red",
            fg="white",
            command=on_delete,
            width=10
        )
        delete_button.pack(side=tk.LEFT, padx=5)
        
        # Store window instance reference
        self.window_instances[button_id] = window_frame


class ButtonNameDialog:
    """Dialog to get button name from user"""
    def __init__(self, parent):
        self.result = None
        
        # Create custom dialog
        dialog = tk.Toplevel(parent)
        dialog.title("Add New Button")
        dialog.geometry("300x150")
        dialog.transient(parent)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = parent.winfo_x() + (parent.winfo_width() - 300) // 2
        y = parent.winfo_y() + (parent.winfo_height() - 150) // 2
        dialog.geometry(f"+{x}+{y}")
        
        # Label
        label = Label(dialog, text="Enter button name:", font=("Arial", 10))
        label.pack(pady=10)
        
        # Entry field
        entry = tk.Entry(dialog, font=("Arial", 10), width=25)
        entry.pack(pady=5, padx=10)
        entry.focus()
        
        # Buttons frame
        button_frame = Frame(dialog)
        button_frame.pack(pady=10)
        
        # OK button
        def ok_clicked():
            name = entry.get().strip()
            if name:
                self.result = name
                dialog.destroy()
            else:
                messagebox.showwarning("Input Error", "Please enter a button name!", parent=dialog)
        
        ok_button = Button(button_frame, text="OK", width=8, command=ok_clicked)
        ok_button.pack(side=tk.LEFT, padx=5)
        
        # Cancel button
        def cancel_clicked():
            self.result = None
            dialog.destroy()
        
        cancel_button = Button(button_frame, text="Cancel", width=8, command=cancel_clicked)
        cancel_button.pack(side=tk.LEFT, padx=5)
        
        # Allow Enter key to confirm
        entry.bind("<Return>", lambda e: ok_clicked())
        
        # Wait for dialog to close
        dialog.wait_window()


if __name__ == "__main__":
    root = tk.Tk()
    app = IntraTradHelper(root)
    root.mainloop()
