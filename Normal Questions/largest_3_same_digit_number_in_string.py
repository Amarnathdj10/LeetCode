class Solution:
    def largestGoodInteger(self, num: str) -> str:
        num_list = ['999', '888', '777', '666', '555', '444', '333', '222', '111', '000', ""]
        for i in num_list:
            if i in num:
                return i
#rework