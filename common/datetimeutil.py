#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: datetimeutil.py
@time: 2021/7/1 0001 11:19
@desc:
'''
import time
import datetime
import calendar

class DateTimeUtil:
    @classmethod
    def getNowTime(cls, format='%Y-%m-%d %H:%M:%S'):
        return datetime.datetime.now().strftime(format)

    @classmethod
    def getNowDate(cls, format='%Y-%m-%d'):
        return datetime.date.today().strftime(format)

    @classmethod
    def getNowTimeStampWithSecond(cls):
        return int(time.time())

    @classmethod
    def getNowTimeStampWithMillisecond(cls):
        return int(round(time.time() * 1000))

    @classmethod
    def getWeekDay(cls):
        """
        获得今天星期几，从1开始
        :return:
        """
        return datetime.datetime.now().weekday() + 1

    @classmethod
    def getHowDaysAgo(cls, nowDateTime, nowDateTime_format='%Y-%m-%d %H:%M:%S', howDaysAgo=0):
        nowDateTime = datetime.datetime.strptime(nowDateTime, nowDateTime_format)
        resultDateTime = nowDateTime - datetime.timedelta(days=howDaysAgo)
        return resultDateTime

    @classmethod
    def dateTimeToStr(cls, theDateTime, format='%Y-%m-%d'):
        return theDateTime.strftime(format)

    @classmethod
    def strToDateTime(cls, str, str_format):
        dst_dateTime = datetime.datetime.strptime(str, str_format)
        return dst_dateTime

    @classmethod
    def getHowYearsAgo(cls, nowDate, howYearsAgo=0, nowDate_format='%Y-%m-%d'):
        resultDate = cls.getHowDaysAgo(nowDate, nowDate_format, howYearsAgo * 366)
        return resultDate

    @classmethod
    def getCurrentMonthFirstDayOrLastDay(cls, type=1):
        """获取当前月第一天或者最后一天日期

        Args:
            type (int, optional): 第一天:1，最后一天:-1

        Returns:
            [type]: [description]
        """
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        last_day = calendar.monthrange(year, month)[1]
        if type == 1:
            start = datetime.date(year, month, 1)
            return start
        if type == -1:
            end = datetime.date(year, month, last_day)
            return end