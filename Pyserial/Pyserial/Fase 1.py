#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 02:09:11 2019

@author: vitor11001
"""

import serial
import config
from importlib import reload

def escrever_porta():
    ser = serial.Serial(config.port_escrita,
                        config.baudrate, 
                        stopbits=config.stopbits)
    
    print(ser.name)
    escrita = str(input('Digite o que deseja escrever: \n'))
    if len(escrita) < config.Bytes:
        for i in range(config.Bytes - len(escrita)):
            escrita = escrita + ' '
    ser.write(escrita.encode(config.encode))
    ser.close()

def ler_porta():
    ser = serial.Serial(config.port_leitura,
                        config.baudrate,
                        #parity = config.parity,
                        timeout = config.timeout,
                        stopbits=config.stopbits)
    print(ser.read(config.Bytes).decode(config.decode))
    ser.close()

def main():    
    while True:

        print('1 - Escrever e enviar pela porta')
        print('2 - Ler entrada da porta')
        print('3 - Atualizar as configurações')
        print('4 - Sair')
        opc = int(input('Escolha a opção: '))
        
        if opc == 1:
            escrever_porta()
        if opc == 2:
            ler_porta()
        if opc == 3:
            reload(config)
        if opc == 4:
            break
           

main()
        
