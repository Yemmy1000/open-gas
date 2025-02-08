
def print_framework_tree_old(): 
    
    # Data organized into three columns
    data = [
        ["Confidentiality", "Data and Information", "Preventative Controls"],
        ["Integrity", "- Data in transit", "- Technical Solutions"],
        ["Availability", "- Data in use", "- Administrative Solutions"],
        ["Authentication", "- Data at rest", "- Physical Security Solutions"],
        ["Authorization", "System and Application", "- Human-Centric Solutions"],
        ["Non-repudiation", "- Hardware", "Detective Controls"],
        ["Accountability", "- Software", "- Technical Solutions"],
        ["Reliability", "Network Infrastructure", "- Administrative Solutions"],
        ["Privacy", "Devices and Endpoints", "- Human-Centric Solutions"],
        ["Resilience", "Applications and Software", "Corrective Controls"],
        ["Possession", "Cloud Services", "- Technical Solutions"],
        ["", "User Accounts and Credentials", "- Operational Solutions"],
        ["", "Physical Assets", "Recovery Controls"],
        ["", "Operational Technology (OT)", "- Operational Solutions"],
        ["", "Intellectual Property and Trade Secrets", "Risk Management"],
        ["", "Communication Channels", "- Administrative Solutions"],
        ["", "Supply Chain and Third-Party Services", "- Legal and Ethical Solutions"],
        ["", "", "- Emerging Technologies"]
    ]

    return data



from tabulate import tabulate
import shutil
def print_framework_tree(): 
    # Get the terminal width
    terminal_width = shutil.get_terminal_size().columns
    
    # Data organized into three columns
    data = [
        ["Confidentiality", "Data and Information", "Preventative Controls"],
        ["Integrity", "- Data in transit", "- Technical Solutions"],
        ["Availability", "- Data in use", "- Administrative Solutions"],
        ["Authentication", "- Data at rest", "- Physical Security Solutions"],
        ["Authorization", "System and Application", "- Human-Centric Solutions"],
        ["Non-repudiation", "- Hardware", "Detective Controls"],
        ["Accountability", "- Software", "- Technical Solutions"],
        ["Reliability", "Network Infrastructure", "- Administrative Solutions"],
        ["Privacy", "Devices and Endpoints", "- Human-Centric Solutions"],
        ["Resilience", "Applications and Software", "Corrective Controls"],
        ["Possession", "Cloud Services", "- Technical Solutions"],
        ["", "User Accounts and Credentials", "- Operational Solutions"],
        ["", "Physical Assets", "Recovery Controls"],
        ["", "Operational Technology (OT)", "- Operational Solutions"],
        ["", "Intellectual Property and Trade Secrets", "Risk Management"],
        ["", "Communication Channels", "- Administrative Solutions"],
        ["", "Supply Chain and Third-Party Services", "- Legal and Ethical Solutions"],
        ["", "", "- Emerging Technologies"]
    ]
    
    # Display the table
    headers = ["Attack Goal", "Target Assets", "Cybersecurity Solution"]
    table = tabulate(data, headers=headers, tablefmt="grid")
    
    # Calculate padding to center the table
    table_width = max(len(line) for line in table.splitlines())
    padding = (terminal_width - table_width) // 2
    
    # Add padding to each line of the table
    centered_table = "\n".join(" " * padding + line for line in table.splitlines())
    
    # Print the centered table
    print(centered_table)