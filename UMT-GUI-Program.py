import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk, ImageFont
import tkinter.font as tkfont

# Create the main window -----------------------------------------------------
windows = tk.Tk()
style = ttk.Style('darkly')
windows.geometry("1440x810")
windows.title("Ultimate Mining Tycoon Calculator")

try:
    icon = tk.PhotoImage(file='SuperCrawler.png')
    windows.iconphoto(True, icon)
except tk.TclError:
    print("Icon file not found. Continuing without icon.")

# Set custom Apple SF Pro font as default because yes
font_path = "Assets/SF-Pro.ttf"
pil_font = ImageFont.truetype(font_path, size=10)
font_name = pil_font.getname()[0]
AppleSFPro = tkfont.Font(family=font_name, size=10)
windows.option_add("*Font", AppleSFPro)
style.configure(".", font=(font_name, 10))

# Tabs -----------------------------------------------------
tabs = ttk.Notebook(windows)

Factory = ttk.Frame(tabs)
Ores = ttk.Frame(tabs)
Machines = ttk.Frame(tabs)
Items = ttk.Frame(tabs)
Transport = ttk.Frame(tabs)

tabs.add(Factory, text='Factory')
tabs.add(Ores, text='Ores')
tabs.add(Machines, text='Machines')
tabs.add(Items, text='Items')
tabs.add(Transport, text='Transport')

tabs.pack(expand=True, fill="both")

# Labels for the tabs
# These labels are used to identify the tabs in the UI
ttk.Label(Factory, text="Factory").grid(
    column=0, row=0, padx=30, pady=0, sticky='w')
ttk.Label(Ores, text="Ores").grid(column=0, row=0, padx=30, pady=30)
ttk.Label(Machines, text="Machines").grid(column=0, row=0, padx=30, pady=30)
ttk.Label(Items, text="Items").grid(column=0, row=0, padx=30, pady=30)
ttk.Label(Transport, text="Transport").grid(column=0, row=0, padx=30, pady=30)

# UI stuff, buttons and textboxs and whatnot -----------------------------------------------------

# Factory tab
Factory.columnconfigure(0, weight=1)
Factory.columnconfigure(1, weight=0)
Factory.columnconfigure(2, weight=1)
Factory.columnconfigure(3, weight=0)
Factory.rowconfigure(0, weight=0)
Factory.rowconfigure(1, weight=0)
Factory.rowconfigure(2, weight=1)
Factory.rowconfigure(3, weight=0)

RightPanel = ttk.Frame(Factory, relief='raised', borderwidth=2)
RightPanel.grid(column=3, row=0, rowspan=4, padx=10, pady=10, sticky='nsew')

RightPanel.columnconfigure(0, weight=1)
RightPanel.columnconfigure(1, weight=0)
RightPanel.columnconfigure(2, weight=1)
RightPanel.columnconfigure(3, weight=0)
RightPanel.rowconfigure(0, weight=1)
RightPanel.rowconfigure(1, weight=0)
RightPanel.rowconfigure(2, weight=1)
RightPanel.rowconfigure(3, weight=0)


# Function to toggle the visibility of the Add Machine Menu
def AddMachineMenuToggle():
    if AddMachineMenu.winfo_ismapped():
        AddMachineMenu.grid_remove()
        RightPanel.grid()
    else:
        AddMachineMenu.grid(column=3, row=0, rowspan=4,
                            padx=10, pady=10, sticky='nsew')
        RightPanel.grid_remove()


# Hide the Add Machine Menu initially
AddMachineMenu = ttk.Frame(Factory, relief='raised', borderwidth=2)
AddMachineMenu.grid(column=3, row=0, rowspan=4,
                    padx=10, pady=10, sticky='nsew')
AddMachineMenu.grid_remove()


# Add buttons to the right panel
# These buttons are used to add machines and items to the factory

# Add Machine Button
AddButton = ttk.Button(RightPanel, text="Add Machine",
                       style='primary.TButton', padding=10, command=AddMachineMenuToggle)
AddButton.configure(width=10)
AddButton.grid(column=0, row=0, padx=10, pady=10, sticky='nw')

# Placeholder button
AddedButton = ttk.Button(RightPanel, text="Ore Cleaner",
                         style='primary.TButton', padding=10, command=lambda: print("*Cleans Ore*"))
AddedButton.configure(width=10)
AddedButton.grid(column=1, row=0, padx=10, pady=10, sticky='nw')


# The Add Machines Menu -----------------------------------------------------
# AddMachineMenu layout configuration
for col in range(3):  # 3 columns: left spacer, content, right spacer
    # Column 1 (center) is wider
    AddMachineMenu.columnconfigure(col, weight=1 if col != 1 else 3)

# Configure rows: 10 total (0–9)
for row in range(10):
    # Rows 1-9 grow, 0 stays static
    AddMachineMenu.rowconfigure(row, weight=1 if 1 <= row <= 9 else 0)

# /\/\/\Column=1, rows 2–9

# Back Button for the Add Machine Menu
AddMachineMenuBackButton = ttk.Button(AddMachineMenu, text="Back",
                                      style='primary.TButton', padding=10, command=AddMachineMenuToggle)
AddMachineMenuBackButton.configure(width=5)
AddMachineMenuBackButton.grid(column=0, row=0, padx=10, pady=10, sticky='nw')

# Resizing the Missing Machine Image
MissingMachineImage = Image.open(r"Assets\NoMachineImage.png")
ResizedMissingImage = MissingMachineImage.resize((300, 300))
# Converting the image to PhotoImage
ResizedMissingImageTk = ImageTk.PhotoImage(ResizedMissingImage)
CrawlerImageLabel = ttk.Label(
    AddMachineMenu, image=ResizedMissingImageTk)
CrawlerImageLabel.grid(column=1, row=2, padx=10,
                       pady=10, sticky='')

# Save Button for the Add Machine Menu
SaveButton = ttk.Button(AddMachineMenu, text="Save",
                        style='primary.TButton', padding=10, command=lambda: print("Machine Saved"))
SaveButton.configure(width=5)
SaveButton.grid(column=3, row=0, padx=10, pady=10, sticky='nw')


# Custom Machine Name Entry
def SaveMachineName():
    machine_name = MachineName.get()
    if machine_name:
        print(f"Machine name '{machine_name}' saved.")
        MachineNameLabel.configure(text=machine_name)

    else:
        print("No machine name entered.")


MachineName = ttk.Entry(AddMachineMenu, font=('AppleSFPro', 10), width=10)
MachineName.grid(column=1, row=3, padx=10, pady=10, sticky='s')

SaveMachineNameButton = ttk.Button(
    AddMachineMenu, text="Save", style='primary.TButton', padding=5, command=SaveMachineName)
SaveMachineNameButton.configure(width=10)
SaveMachineNameButton.grid(column=1, row=3, padx=10, pady=10, sticky='es')

MachineNameLabel = ttk.Label(
    AddMachineMenu, text="Machine Name", font=('AppleSFPro', 15))
MachineNameLabel.grid(column=1, row=3, padx=10, pady=10, sticky='n')

MachineSetnameLabel = ttk.Label(
    AddMachineMenu, text="Set Name", font=('AppleSFPro', 10))
MachineSetnameLabel.grid(column=1, row=3, padx=50, pady=13, sticky='ws')


# Custom Machine Money Entry
def SaveMachinePrice():
    machine_money = MachineMoney.get()
    if machine_money:
        print(f"Machine Price '{machine_money}$' saved.")
        MachineMoneySetPriceLabel.configure(text=f"{machine_money}$")
    else:
        print("No Price entered.")


MachineMoney = ttk.Entry(AddMachineMenu, font=('AppleSFPro', 10), width=10)
MachineMoney.grid(column=1, row=4, padx=10, pady=10, sticky='s')

MachineMoneySetPriceLabel = ttk.Label(
    AddMachineMenu, text="Set Price", font=('AppleSFPro', 15))
MachineMoneySetPriceLabel.grid(column=1, row=4, padx=10, pady=10, sticky='n')

MachineMoneyLabel = ttk.Label(
    AddMachineMenu, text="Enter Price", font=('AppleSFPro', 10))
MachineMoneyLabel.grid(column=1, row=4, padx=43, pady=13, sticky='ws')

SaveMachineMoneyButton = ttk.Button(
    AddMachineMenu, text="Save", style='primary.TButton', padding=5, command=SaveMachinePrice)
SaveMachineMoneyButton.configure(width=10)
SaveMachineMoneyButton.grid(column=1, row=4, padx=10, pady=10, sticky='es')


# Factory Plot Test, doesnt do anything yet, jusr a placeholder
BaseFactoryPlot = Image.open(r"Assets\Factory-Plot.png")
FactoryPlot = BaseFactoryPlot.resize((800, 800))

FactoryPlot = ImageTk.PhotoImage(FactoryPlot)
FactoryPlotLabel = ttk.Label(Factory, image=FactoryPlot)
FactoryPlotLabel.grid(column=2, row=2, padx=10, pady=10, sticky='nsew')

# Layer Text Test, same as above, just a placeholder
LayerText = ttk.Label(Factory, text="Layer 1", font=('AppleSFPro', 20))
LayerText.grid(column=2, row=2, padx=10, pady=10, sticky='e')


windows.mainloop()
