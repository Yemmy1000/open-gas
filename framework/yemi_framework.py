
framework_component = ['Breaches', 'Attack Target Assets', 'Cybersecurity Solutions']

breaches = {
    0:'Confidentiality', 1:'Integrity', 2:'Availability', 3:'Authentication', 4:'Authorization', 5:'Non-repudiation', 6:'Accountability', 7:'Reliability', 8:'Privacy', 9:'Resilience', 10:'Possession'
    }

goal_descr = {
    0: ['Unauthorized access to sensitive data', 'Data leaks or breaches', 'Eavesdropping on communications'],
    1: ['Data tampering or alteration', 'Unauthorized changes to systems or software', 'Injection of malicious code'],
    2: ['Denial of Service (DoS) attacks', 'Distributed Denial of Service (DDoS) attacks', 'Disruption of services or network operations'],
    3: ['Unauthorized access to systems through credential theft', 'Impersonation or spoofing attacks', 'Breaches of authentication mechanisms'],
    4: ['Escalation of privileges', 'Unauthorized actions or access', 'Circumventing access controls'],
    5: ['Falsifying transaction records', 'Denying legitimate transactions', 'Tampering with audit logs'],
    6: ['Erasing or altering audit trails', 'Disguising or hiding malicious activities', 'Avoiding detection and traceability'],
    7: ['Causing system malfunctions or failures', 'Introducing errors into data or processes', 'Interrupting critical operations'],
    8: ['Collecting personal information without consent', 'Surveillance and tracking activities', 'Misuse of personal data'],
    9: ['Exploiting vulnerabilities to cause persistent damage', 'Targeting backup systems and recovery processes', 'Preventing or delaying recovery efforts'],
    10: ['Unauthorized access attacks', 'Stolen devices', 'Insider threats'],
}

target_assets = {
    0:'Data and Information', 1: 'Network Infrastructure', 2: 'Devices and Endpoints', 3: 'Applications and Software',
    4: 'Cloud Services', 5: 'User Accounts and Credentials', 6: 'Physical Assets', 7: 'Operational Technology (OT)',
    8: 'Intellectual Property and Trade Secrets', 9: 'Communication Channels', 10: 'Supply Chain and Third-Party Services'
}

target_assets_descr = {
    0: ['Personal Data (PII - Personally Identifiable Information)', 'Financial Data', 'Intellectual Property', 'Operational Data', 'Health Information (PHI - Protected Health Information)'],
    1: ['Routers', 'Switches', 'Firewalls', 'Load Balancers', 'Network Cables'],
    2: ['Computers (Desktops, Laptops)', 'Mobile Devices (Smartphones, Tablets)', 'Servers', 'IoT Devices', 'Wearables'],
    3: ['Operating Systems', 'Business Applications (CRM, ERP)', 'Databases', 'Web Applications', 'Mobile Apps'],
    4: ['Cloud Storage', 'SaaS (Software as a Service)', 'PaaS (Platform as a Service)', 'IaaS (Infrastructure as a Service)'],
    5: ['Employee Accounts', 'Customer Accounts', 'Administrative Accounts', 'API Keys'],
    6: ['Data Centers', 'Physical Servers', 'Laptops and Workstations', 'USB Drives and External Storage'],
    7: ['Industrial Control Systems (ICS)', 'SCADA Systems (Supervisory Control and Data Acquisition)', 'PLCs (Programmable Logic Controllers)', 'Robotics'],
    8: ['Patents', 'Designs', 'Proprietary Processes', 'Research and Development Data'],
    9: ['Email Systems', 'Instant Messaging', 'Video Conferencing', 'VoIP Systems'],
    10: ['Partner Networks', 'Vendor Systems', 'Third-Party Service Providers']
}

cybersecurity_Solution = {
    0:'Preventative Controls', 1: 'Detective Controls', 2: 'Corrective Controls', 3: 'Recovery Controls', 4: 'Risk Management' 
    }

cybersecurity_solution_descr = [
    {
        'Technical Solutions': ['Firewalls', 'Antivirus and Anti-Malware Software', 'Encryption', 'Endpoint Protection', 'Multi-factor Authentication (MFA)', 'Network Segmentation'],
        'Administrative Solutions': ['Security Policies and Procedures', 'Access Control (Role-Based Access Control, Least Privilege)', 'Compliance and Regulatory Adherence'],
        'Physical Security Solutions': ['Secure Facilities', 'Device Security', 'Environmental Controls'],
        'Human-Centric Solutions': ['Security Awareness Training', 'Phishing Simulations']
    },
    {
        'Technical Solutions': ['Intrusion Detection Systems (IDS)', 'Monitoring and Logging', 'Threat Intelligence'],
        'Administrative Solutions': ['Regular Audits and Assessments'],
        'Human-Centric Solutions': ['Insider Threat Management']
    },
    {
        'Technical Solutions': ['Intrusion Prevention Systems (IPS)', 'Patch Management'],
        'Operational Solutions': ['Incident Response Planning', 'Ethical Hacking (to identify and address vulnerabilities)']
    },

    {
        'Operational Solutions': ['Backup and Recovery', 'Disaster Recovery Planning'],
    },
    {
        'Administrative Solutions': ['Security Policies and Procedures', 'Compliance and Regulatory Adherence'],
        'Legal and Ethical Solutions': ['Cyber Insurance', 'Legal Action and Enforcement'],
        'Emerging Technologies': ['Artificial Intelligence and Machine Learning (for advanced threat detection and response)', 'Blockchain Technology (for secure transactions and data integrity)', 'Zero Trust Architecture (for verifying every access request)']

    }

]


Preventative_Controls = {
        'Technical Solutions': ['Firewalls', 'Antivirus and Anti-Malware Software', 'Encryption', 'Endpoint Protection', 'Multi-factor Authentication (MFA)', 'Network Segmentation'],
        'Administrative Solutions': ['Security Policies and Procedures', 'Access Control (Role-Based Access Control, Least Privilege)', 'Compliance and Regulatory Adherence'],
        'Physical Security Solutions': ['Secure Facilities', 'Device Security', 'Environmental Controls'],
        'Human-Centric Solutions': ['Security Awareness Training', 'Phishing Simulations']
    }

Detective_Controls =   {
        'Technical Solutions': ['Intrusion Detection Systems (IDS)', 'Monitoring and Logging', 'Threat Intelligence'],
        'Administrative Solutions': ['Regular Audits and Assessments'],
        'Human-Centric Solutions': ['Insider Threat Management']
    }



Corrective_Controls =  {
        'Technical Solutions': ['Intrusion Prevention Systems (IPS)', 'Patch Management'],
        'Operational Solutions': ['Incident Response Planning', 'Ethical Hacking (to identify and address vulnerabilities)']
    }


Recovery_Controls =   {
        'Operational Solutions': ['Backup and Recovery', 'Disaster Recovery Planning'],
    }


Risk_Management =  {
        'Administrative Solutions': ['Security Policies and Procedures', 'Compliance and Regulatory Adherence'],
        'Legal and Ethical Solutions': ['Cyber Insurance', 'Legal Action and Enforcement'],
        'Emerging Technologies': ['Artificial Intelligence and Machine Learning (for advanced threat detection and response)', 'Blockchain Technology (for secure transactions and data integrity)', 'Zero Trust Architecture (for verifying every access request)']

    }




