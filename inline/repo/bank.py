banks = [

    {
        "name": "招商银行",
        "card_no": "1a"
    },
    {
        "name": "招商银行",
        "card_no": "1b"
    },
    {
        "name": "招商银行信用卡",
        "card_no": "11"
    },
    {
        "name": "建设银行",
        "card_no": "2a"
    },
]


class Bank(object):
    """
        银行卡类
    """

    def __init__(self, name, card_no):
        self.__name = name
        self.__card_no = card_no

    def get_name(self):
        return self.__name

    def get_card_no(self):
        return self.__card_no

    def __str__(self) -> str:
        return "Bank Object (name:%s,card_no:%s)" % (self.get_name(), self.get_card_no())


def to_dict(banks_str):
    banks_dict = {}
    for obj in banks_str:
        bank = Bank(obj["name"], obj["card_no"])
        banks_list = banks_dict.get(bank.get_name())
        if not banks_list:
            banks_list = [bank]
        else:
            banks_list.append(bank)
        banks_dict[bank.get_name()] = banks_list
    return banks_dict


banks = to_dict(banks)
