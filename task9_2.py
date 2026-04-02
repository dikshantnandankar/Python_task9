class Insurance:
    def __init__(self,name,age,sum_insured,risk_level,smoker,drinker,addons= None,no_claim_bonus = False):
        self.cust_name = name
        self.cust_age = age
        self.cust_sum_insured = sum_insured
        self.cust_risk_level = risk_level
        self.smoke_status = smoker
        self.drink_status = drinker
        self.add_ons = addons
        self.no_claim_bonus_status = no_claim_bonus

    def cust_details(self):
        return {
            'cust_name' : self.cust_name,
            'cust_age' : self.cust_age,
            'cust_sum_insured' : self.cust_sum_insured,
            'cust_risk_level' : self.cust_risk_level,
            'smoke_status' : self.smoke_status,
            'drink_status' : self.drink_status,
            'add_ons' : self.add_ons,
            'no_claim_bonus_status' : self.no_claim_bonus_status
        }

    def get_age_factor(self):
        if self.cust_age < 18:
            return 1.0
        elif self.cust_age < 30:
            return 1.2
        elif self.cust_age < 45:
            return 1.5
        elif self.cust_age < 60:
            return 1.75
        else:
            return 2.0
        
    def get_risk_factor(self):
        if self.cust_risk_level == 'low':
            return 0
        elif self.cust_risk_level == 'medium':
            return 0.1
        elif self.cust_risk_level == 'high':
            return 0.2
        else :
            return 0.25
        
    def get_add_ons(self):
        addon_price = {
            'critical' : 2000,
            'accidental' : 1500
        }
        return sum(addon_price.get(a,0)
                   for a in self.add_ons)
    
class Premium(Insurance):
    def __init__(self, premium_details):
        super().__init__(premium_details.get('cust_name'), premium_details.get('cust_age'),
                         premium_details.get('cust_sum_insured'), premium_details.get('cust_risk_level'),
                           premium_details.get('smoke_status'), premium_details.get('drink_status'), 
                           premium_details.get('add_ons'), premium_details.get('no_claim_bonus_status'))
        
    def premium_calculate(self):
        print('This is premium calculated for customer')
        base_premium = 5000
        age_factor = self.get_age_factor()
        sum_factor = self.cust_sum_insured / 100000

        premium = base_premium * age_factor * sum_factor
        if self.smoke_status == True:
            risk = self.get_risk_factor()
            risk_amount = premium * risk
            premium = premium + risk_amount
        else :
            premium = premium

        if self.drink_status == True:
            risk = self.get_risk_factor()
            risk_amount = premium * risk
            premium = premium + risk_amount
        else : 
            premium =   premium
        
        premium = premium + self.get_add_ons()

        if self.no_claim_bonus_status == True:
            premium = premium * 0.1
        else:
            premium = premium
        return round(premium,2)
    
    def get_cust_details(self):
        getcustdetails = self.cust_details()
        print('This is Customer Insurance details')
        return {
            'cust_name' : getcustdetails.get('cust_name'),
            'cust_age' : getcustdetails.get('cust_age'),
            'cust_sum_insured' : getcustdetails.get('cust_sum_insured'),
            'cust_risk_level' : getcustdetails.get('cust_risk_level'),
            'smoke_status' : getcustdetails.get('smoke_status'),
            'drink_status' : getcustdetails.get('drink_status'),
            'add_ons' : getcustdetails.get('add_ons'),
            'no_claim_bonus_status' : getcustdetails.get('no_claim_bonus_status')
        }
    
cust_details = [{
    'cust_name' : 'Anand',
    'cust_age' : 28,
    'cust_sum_insured' : 3000000,
    'cust_risk_level' : 'medium',
    'smoke_status' : True,
    'drink_status' : True,
    'add_ons' : 'critical',
    'no_claim_bonus_status' : True
},
{
    'cust_name' : 'Vicky',
    'cust_age' : 32,
    'cust_sum_insured' : 3000000,
    'cust_risk_level' : 'medium',
    'smoke_status' : True,
    'drink_status' : True,
    'add_ons' : 'critical',
    'no_claim_bonus_status' : True
}]

i1 = Premium(cust_details[1])
print(i1.get_cust_details())
print(i1.premium_calculate())



