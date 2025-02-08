from framework.yemi_framework import * 
from cot.response_storage import ResponseStorage
responseStorage = ResponseStorage()


class ChainOfThought:
    def __init__(self):
        self.stage = 0
        self.user_input = ""
    
    def start_conversation(self):
        self.stage = 0
        greet = ['Welcome to Open-GAS: An AI-based asisistive tool for security experts', 'I will assist you using a model based on the outline:']

        return greet
    
    def process_input(self, user_input, response):
        if self.stage == 0:
            return self.handle_initial_query(user_input)
        elif self.stage == 1:
            # call AI to investigate
            return self.attack_goal(user_input, response)
        
        elif self.stage == 2:
            # call AI to investigate
            return self.attack_asset(user_input, response)
        elif self.stage == 3:
            # call AI to investigate
            return self.cybersecurity_solution(user_input, response)
        
        else:
            return self.final_thoughts(user_input, response)

        # elif self.stage == 310:
        #     return self.handle_action(user_input)
    
    def handle_initial_query(self, user_input):
        if user_input != '':
            self.stage = self.stage+1
            return user_input
        else:
            return "I'm not sure how to assist with that. Can you please provide more details?"
    
    def handle_investigation(self, user_input):
        print(user_input)
        # Implement investigation logic
        return "Investigation details processed. What action would you like to take next?"
    
    def handle_action(self, user_input):
        # Implement action logic
        return "Action taken based on threat analysis. Is there anything else you need?"


    def attack_goal(self, user_input, response):
        prompt = f"Consider this scenario: {user_input}. What is the attacker aim to breach from the following {breaches}, and what is the attack goals\n "
        responseStorage.add_mapping("incidence: " + user_input, self.stage)    
        self.stage = self.stage+1
        # print(responseStorage.get_all_mappings())
        return prompt
    
    def attack_asset(self, user_input, response):
        # print("Response: "+ response)
        history = responseStorage.get_all_mappings()
        prompt = f"Consider this scenario: {history}. What category of assets are at risk from the following {target_assets}, you may give example of assets from each category identified. \n "  
        responseStorage.add_mapping("Response on attack goals: " + response, self.stage)  
        self.stage = self.stage+1
        return prompt
    
    def cybersecurity_solution(self, user_input, response):
        history = responseStorage.get_all_mappings()
        prompt = f"Consider this incident analysis history: {history}. \n "  
        responseStorage.add_mapping("Response on affected assets: " + response , self.stage)  
        self.stage = self.stage+1

        prompt = prompt + f"Assistive solution will be provided using the following  {cybersecurity_solution_descr}, taking step by step."
            # Add more context
        return prompt
    
    def preventive_control(self, user_input, response, count=0):        
        history = responseStorage.get_all_mappings() 
        responseStorage.add_mapping("Assistive solution: " + response , self.stage)  
        self.stage = self.stage+1
        myKey = list(Preventative_Controls.keys())[count]
        prompt = f"Consider this incident analysis history: {history}. \n \
        Your role is to assist in providing {myKey} for preventive controls using any or all components of this guide {Preventative_Controls[myKey]} where necessary.\n \
        Important: {user_input} \n" 

        return prompt
        # return 'proceed'
    def detective_controls(self, user_input, response, count=0):        
        history = responseStorage.get_all_mappings() 
        responseStorage.add_mapping("Assistive solution: " + response , self.stage)  
        self.stage = self.stage+1
        myKey = list(Detective_Controls.keys())[count]
        prompt = f"Consider this incident analysis history: {history}. \n \
        Your role is to assist in providing {myKey} for detective controls using any or all components of this guide {Detective_Controls[myKey]} where necessary.\n \
        Important: {user_input} \n" 

        return prompt    


    def corrective_controls(self, user_input, response, count=0):        
        history = responseStorage.get_all_mappings() 
        responseStorage.add_mapping("Assistive solution: " + response , self.stage)  
        self.stage = self.stage+1
        myKey = list(Corrective_Controls.keys())[count]
        prompt = f"Consider this incident analysis history: {history}. \n \
        Your role is to assist in providing {myKey} for corrective controls using any or all components of this guide {Corrective_Controls[myKey]} where necessary.\n \
        Important: {user_input} \n" 

        return prompt  
    
    def recovery_controls(self, user_input, response, count=0):        
        history = responseStorage.get_all_mappings() 
        responseStorage.add_mapping("Assistive solution: " + response , self.stage)  
        self.stage = self.stage+1
        myKey = list(Recovery_Controls.keys())[count]
        prompt = f"Consider this incident analysis history: {history}. \n \
        Your role is to assist in providing {myKey} for recovery controls using any or all components of this guide {Recovery_Controls[myKey]} where necessary.\n \
        Important: {user_input} \n" 

        return prompt      

    def risk_management(self, user_input, response, count=0):        
        history = responseStorage.get_all_mappings() 
        responseStorage.add_mapping("Assistive solution: " + response , self.stage)  
        self.stage = self.stage+1
        myKey = list(Risk_Management.keys())[count]
        prompt = f"Consider this incident analysis history: {history}. \n \
        Your role is to assist in providing {myKey} for risk management using any or all components of this guide {Risk_Management[myKey]} where necessary.\n \
        Important: {user_input} \n" 
        # print(prompt)
        return prompt    


    def final_thoughts(self, user_input, response, count=0):
        history = responseStorage.get_all_mappings() 
        responseStorage.add_mapping("Final thoughts: " + response , self.stage)  
        prompt = f"Consider this incident analysis history: {history}. \n \
        Your role is to assist in summarizing in form of final thoughts.\n \
        Important: {user_input} \n" 
        # print(prompt)
        return prompt    





    # def cybersecurity_Solution(self, user_input, response):
    #     history = responseStorage.get_all_mappings()
    #     prompt = f"Consider this incident analysis history: {history}. \n "  
    #     responseStorage.add_mapping("Response on affected assets: " + response , self.stage)  
    #     self.stage = self.stage+1

    #     for k, v in cybersecurity_Solution.items():
    #         guide = cybersecurity_solution_descr[k]
    #         more_context = input("I am about to provide" + str(v) + str(guide))
    #         prompt = prompt + f"Your role is to provide {v} using the component of this guide {guide} where necessary. Where technical solution is required, write codes and mention all tools needed."
    #         # Add more context
    #     return prompt


# cybersecurity_Solution = {
#     0:'Preventative Controls', 1: 'Detective Controls', 2: 'Corrective Controls', 3: 'Recovery Controls', 4: 'Risk Management' 
#     }


# cybersecurity_solution_descr = [
#     {
#         'Technical Solutions': ['Firewalls', 'Antivirus and Anti-Malware Software', 'Encryption', 'Endpoint Protection', 'Multi-factor Authentication (MFA)', 'Network Segmentation'],
#         'Administrative Solutions': ['Security Policies and Procedures', 'Access Control (Role-Based Access Control, Least Privilege)', 'Compliance and Regulatory Adherence'],
#         'Physical Security Solutions': ['Secure Facilities', 'Device Security', 'Environmental Controls'],
#         'Human-Centric Solutions': ['Security Awareness Training', 'Phishing Simulations']
#     }
# ]
        # elif self.stage == 2:
        #     return self.handle_action(user_input)




# Example usage
# cot = ChainOfThought()
# print(cot.start_conversation())
# user_input = "I have a security incident"
# print(cot.process_input(user_input))
# user_input = "It's a potential breach"
# print(cot.process_input(user_input))
