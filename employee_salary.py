from abc import ABC, abstractmethod

class employee(ABC):
    @abstractmethod
    def cal_salary(self):
        pass
class intern(employee):
    def cal_salary(self):
        return 15000

class full_time(employee):
    def cal_salary(self):
        return 20000

class contract_based(employee):
    def cal_salary(self):
        return 35000

inte = intern()
full = full_time()
contract = contract_based()

print("the intern salary is",inte.cal_salary())
print("the full_time salary is",full.cal_salary())
print("the  contract_based salary is",contract.cal_salary())
