from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from enum import Enum
import random
import json
author = 'FuHsuan Tsai'

doc = """
複製實驗——未來式：問卷主體
"""
class WaitingPeriod(object):
    list = [10, 20, 40, 80, 54, 64, 84, 124]

class GainedAmount(object):
    today = 100

class Treatment(object):
    futureTense = "將"
    def get_treatment(player):
        participant = player.participant
        # lazy loading: 若不存在就決定並起來，若已存在就直接取出
        if Constants.key_method not in participant.vars:
            """ 步驟四：將control跟treatmentWill隨機選擇，存進participant.vars中"""

        method = participant.vars[Constants.key_method]
        return method


class Constants(BaseConstants):
    name_in_url = 'Exp1_questionaire'
    players_per_group = None
    gainedamount_sooner = GainedAmount.today
    num_rounds = 8
    key_params = 'questionnaire_parameters'  # 儲存等待週次順序
    key_method = 'treatment_method'  # 儲存是控制組或是實驗組
    futureTense = Treatment.futureTense

class OptionOfGetMoney(object):
    part1 = '於'
    part2 = '星期後，'
    part3 = '收到'

    def formatted_option(player, part1, part2, part3):
        if player.treatment_method == "control":
            return part1, part2 + part3
        elif player.treatment_method == "treatmentWill":
            """ 步驟五：判斷結果為實驗組時，應回傳的內容"""
            return

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.treatment_method = Treatment.get_treatment(p)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    waiting_period = models.IntegerField()
    treatment_method = models.StringField()
    sooner_period = models.StringField()

    switch_point = models.StringField(
        label = '請選擇您的轉換點',
        widget = widgets.RadioSelect,
    )
    
    def switch_point_choices(self):
        options_part1, options_part2 = OptionOfGetMoney.formatted_option(self, OptionOfGetMoney.part1, OptionOfGetMoney.part2, OptionOfGetMoney.part3)
        """ 步驟六：將結果組合成完整的句子（放入該回合等待的週數）"""
        options =
        
        """ 步驟七：回傳選項，應以選項1-9儲存於data，而非完整之選項敘述"""
        return [









        ]
