#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 18:55:08 2019

@author: vitor11001
"""
import serial

#Porta de Escrita
port_escrita = 'COM1'

#Porta de Leitura
port_leitura = 'COM2'

#Baud Rate
baudrate = 9600

#Bit de parada
stopbits=serial.STOPBITS_ONE

#Paridade
parity = serial.PARITY_EVEN

#Limite de tempo em escuta
timeout = 10

#Numero de Bytes escutaveis
Bytes = 10

#codificaçao da mensagem
encode = 'ascii'

#decodificaçao da mensagem
decode = 'ascii'
