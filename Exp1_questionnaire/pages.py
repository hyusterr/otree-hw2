from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, WaitingPeriod, GainedAmount
from random import randint
import random

class Questionnaire(Page):
    form_model = 'player'
    form_fields = [
        'waiting_period',
        'sooner_period',
        'treatment_method',
        'switch_point',
        ]

    def generate_questionnaire_parameters(self):
        """ 步驟二：取得等待週數的list，並打亂順序後回傳"""


        return shuffled_waiting_period

    def setup_questionaire_parameters_pairs(self):
        # 如果還不存在，就現在產生「週數的順序」並存起來
        # 如果已經存在，就取出
        if Constants.key_params not in self.participant.vars:
            shuffled_waiting_period = self.generate_questionnaire_parameters()
            self.participant.vars[Constants.key_params] = shuffled_waiting_period
        params = self.participant.vars[Constants.key_params]

        # 設定每一 round 的參數，並寫入 db
        idx = self.round_number - 1 # list 從0開始 但 round_bnumber 從1開始
        """ 步驟三：取得該回合的等待週數、存進player的waiting_period中"""

        sooner_period = int(params[idx] % 10)
        
        if sooner_period == 0:
            self.player.sooner_period = '今天'
        elif sooner_period == 4:
            self.player.sooner_period = '4星期後'
            
    def is_displayed(self): # 一定會跑的
        # 設定每一 round 的參數（如週數和金額）
        """ 步驟一：執行setup_questionaire_parameters_pairs，來分配週數"""

        return True

page_sequence = [Questionnaire]
