## Транслятор asm и модель процессора. Архитектура Компьютера

- Налобин Александр Николаевич P3230    
- `asm | acc | harv | hw | instr | struct | stream | port | pstr | prob2`
- Без усложнения 

## Язык программирования

``` ebnf
<program> ::= { <line> }

<line> ::= <label> [ <comment> ] "\n"
         | <instr> [ <comment> ] "\n"
         | [ <comment> ] "\n"

<label> ::= <label_name> ":"

<instr> ::= <op0>
          | <op1> <label_name>

<op0> ::= "inc"
        | "dec"
        | "shr"
        | "shl"
        | "print"
        | "input"

<op1> ::= "jmp"
        | "jz"

<integer> ::= [ "-" ] <digit> { <digit> }

<label_name> ::= <letter> { <letter> | <digit> | "_" }

<comment> ::= ";" { <any symbols except "\n"> }

<digit> ::= "0-9"

<letter> ::= "a-z A-Z"
```


## Организация памяти

## Система команд

## Транслятор

## Модель процессора

## Тестирование