import config
import random
from pyrogram import filters
from pyrogram.types import *
from NandhaBot import bot

QUOTES_IMG = (
      "https://i.imgur.com/Iub4RYj.jpg", 
      "https://i.imgur.com/uvNMdIl.jpg", 
      "https://i.imgur.com/YOBOntg.jpg", 
      "https://i.imgur.com/fFpO2ZQ.jpg", 
      "https://i.imgur.com/f0xZceK.jpg", 
      "https://i.imgur.com/RlVcCip.jpg", 
      "https://i.imgur.com/CjpqLRF.jpg", 
      "https://i.imgur.com/8BHZDk6.jpg", 
      "https://i.imgur.com/8bHeMgy.jpg", 
      "https://i.imgur.com/5K3lMvr.jpg", 
      "https://i.imgur.com/NTzw4RN.jpg", 
      "https://i.imgur.com/wJxryAn.jpg", 
      "https://i.imgur.com/9L0DWzC.jpg", 
      "https://i.imgur.com/sBe8TTs.jpg", 
      "https://i.imgur.com/1Au8gdf.jpg", 
      "https://i.imgur.com/28hFQeU.jpg", 
      "https://i.imgur.com/Qvc03JY.jpg", 
      "https://i.imgur.com/gSX6Xlf.jpg", 
      "https://i.imgur.com/iP26Hwa.jpg", 
      "https://i.imgur.com/uSsJoX8.jpg", 
      "https://i.imgur.com/OvX3oHB.jpg", 
      "https://i.imgur.com/JMWuksm.jpg", 
      "https://i.imgur.com/lhM3fib.jpg", 
      "https://i.imgur.com/64IYKkw.jpg", 
      "https://i.imgur.com/nMbyA3J.jpg", 
      "https://i.imgur.com/7KFQhY3.jpg", 
      "https://i.imgur.com/mlKb7zt.jpg", 
      "https://i.imgur.com/JCQGJVw.jpg", 
      "https://i.imgur.com/hSFYDEz.jpg", 
      "https://i.imgur.com/PQRjAgl.jpg", 
      "https://i.imgur.com/ot9624U.jpg", 
      "https://i.imgur.com/iXmqN9y.jpg", 
      "https://i.imgur.com/RhNBeGr.jpg", 
      "https://i.imgur.com/tcMVNa8.jpg", 
      "https://i.imgur.com/LrVg810.jpg", 
      "https://i.imgur.com/TcWfQlz.jpg", 
      "https://i.imgur.com/muAUdvJ.jpg", 
      "https://i.imgur.com/AtC7ZRV.jpg", 
      "https://i.imgur.com/sCObQCQ.jpg", 
      "https://i.imgur.com/AJFDI1r.jpg", 
      "https://i.imgur.com/TCgmRrH.jpg", 
      "https://i.imgur.com/LMdmhJU.jpg", 
      "https://i.imgur.com/eyyax0N.jpg", 
      "https://i.imgur.com/YtYxV66.jpg", 
      "https://i.imgur.com/292w4ye.jpg", 
      "https://i.imgur.com/6Fm1vdw.jpg", 
      "https://i.imgur.com/2vnBOZd.jpg", 
      "https://i.imgur.com/j5hI9Eb.jpg", 
      "https://i.imgur.com/cAv7pJB.jpg", 
      "https://i.imgur.com/jvI7Vil.jpg", 
      "https://i.imgur.com/fANpjsg.jpg", 
      "https://i.imgur.com/5o1SJyo.jpg", 
      "https://i.imgur.com/dSVxmh8.jpg", 
      "https://i.imgur.com/02dXlAD.jpg", 
      "https://i.imgur.com/htvIoGY.jpg", 
      "https://i.imgur.com/hy6BXOj.jpg", 
      "https://i.imgur.com/OuwzNYu.jpg", 
      "https://i.imgur.com/L8vwvc2.jpg", 
      "https://i.imgur.com/3VMVF9y.jpg", 
      "https://i.imgur.com/yzjq2n2.jpg", 
      "https://i.imgur.com/0qK7TAN.jpg", 
      "https://i.imgur.com/zvcxSOX.jpg", 
      "https://i.imgur.com/FO7bApW.jpg", 
      "https://i.imgur.com/KK06gwg.jpg", 
      "https://i.imgur.com/6lG4tsO.jpg"
      
      ) 

reactions = [
    "( ͡° ͜ʖ ͡°)", "( . •́ _ʖ •̀ .)", "( ಠ ͜ʖ ಠ)", "( ͡ ͜ʖ ͡ )", "(ʘ ͜ʖ ʘ)",
    "ヾ(´〇`)ﾉ♪♪♪", "ヽ(o´∀`)ﾉ♪♬", "♪♬((d⌒ω⌒b))♬♪", "└(＾＾)┐", "(￣▽￣)/♫•*¨*•.¸¸♪",
    "ヾ(⌐■_■)ノ♪", "乁( • ω •乁)", "♬♫♪◖(● o ●)◗♪♫♬", "(っ˘ڡ˘ς)", "( ˘▽˘)っ♨",
    "(　・ω・)⊃-[二二]", "(*´ー`)旦 旦(￣ω￣*)", "( ￣▽￣)[] [](≧▽≦ )", "(*￣▽￣)旦 且(´∀`*)",
    "(ノ ˘_˘)ノ　ζ|||ζ　ζ|||ζ　ζ|||ζ", "(ノ°∀°)ノ⌒･*:.｡. .｡.:*･゜ﾟ･*☆",
    "(⊃｡•́‿•̀｡)⊃━✿✿✿✿✿✿", "(∩` ﾛ ´)⊃━炎炎炎炎炎", "( ・∀・)・・・--------☆",
    "( -ω-)／占~~~~~", "○∞∞∞∞ヽ(^ー^ )", "(*＾＾)/~~~~~~~~~~◎", "((( ￣□)_／",
    "(ﾒ￣▽￣)︻┳═一", "ヽ( ･∀･)ﾉ_θ彡☆Σ(ノ `Д´)ノ", "(*`0´)θ☆(メ°皿°)ﾉ",
    "(; -_-)――――――C<―_-)", "ヽ(>_<ヽ) ―⊂|=0ヘ(^‿^ )", "(҂` ﾛ ´)︻デ═一 ＼(º □ º l|l)/",
    "/( .□.)＼ ︵╰(°益°)╯︵ /(.□. /)", "(`⌒*)O-(`⌒´Q)", "(っ•﹏•)っ ✴==≡눈٩(`皿´҂)ง",
    "ヾ(・ω・)メ(・ω・)ノ", "(*^ω^)八(⌒▽⌒)八(-‿‿- )ヽ", "ヽ( ⌒ω⌒)人(=^‥^= )ﾉ",
    "｡*:☆(・ω・人・ω・)｡:゜☆｡", "(°(°ω(°ω°(☆ω☆)°ω°)ω°)°)", "(っ˘▽˘)(˘▽˘)˘▽˘ς)",
    "(*＾ω＾)人(＾ω＾*)", "＼(▽￣ \ (￣▽￣) / ￣▽)／", "(￣Θ￣)", "＼( ˋ Θ ´ )／",
    "( ´(00)ˋ )", "＼(￣(oo)￣)／", "／(≧ x ≦)＼", "／(=･ x ･=)＼", "(=^･ω･^=)",
    "(= ; ｪ ; =)", "(=⌒‿‿⌒=)", "(＾• ω •＾)", "ଲ(ⓛ ω ⓛ)ଲ", "ଲ(ⓛ ω ⓛ)ଲ", "(^◔ᴥ◔^)",
    "[(－－)]..zzZ", "(￣o￣) zzZZzzZZ", "(＿ ＿*) Z z z", "☆ﾐ(o*･ω･)ﾉ",
    "ε=ε=ε=ε=┌(;￣▽￣)┘", "ε===(っ≧ω≦)っ", "__φ(．．)", "ヾ( `ー´)シφ__", "( ^▽^)ψ__",
    "|･ω･)", "|д･)", "┬┴┬┴┤･ω･)ﾉ", "|･д･)ﾉ", "(*￣ii￣)", "(＾〃＾)", "m(_ _)m",
    "人(_ _*)", "(シ. .)シ", "(^_~)", "(>ω^)", "(^_<)〜☆", "(^_<)", "(づ￣ ³￣)づ",
    "(⊃｡•́‿•̀｡)⊃", "⊂(´• ω •`⊂)", "(*・ω・)ﾉ", "(^-^*)/", "ヾ(*'▽'*)", "(^０^)ノ",
    "(*°ｰ°)ﾉ", "(￣ω￣)/", "(≧▽≦)/", "w(°ｏ°)w", "(⊙_⊙)", "(°ロ°) !", "∑(O_O;)",
    "(￢_￢)", "(¬_¬ )", "(↼_↼)", "(￣ω￣;)", "┐('～`;)┌", "(・_・;)", "(＠_＠)",
    "(•ิ_•ิ)?", "ヽ(ー_ー )ノ", "┐(￣ヘ￣)┌", "┐(￣～￣)┌", "┐( ´ д ` )┌", "╮(︶▽︶)╭",
    "ᕕ( ᐛ )ᕗ", "(ノωヽ)", "(″ロ゛)", "(/ω＼)", "(((＞＜)))", "~(>_<~)", "(×_×)",
    "(×﹏×)", "(ノ_<。)", "(μ_μ)", "o(TヘTo)", "( ﾟ，_ゝ｀)", "( ╥ω╥ )", "(／ˍ・、)",
    "(つω`｡)", "(T_T)", "o(〒﹏〒)o", "(＃`Д´)", "(・`ω´・)", "( `ε´ )", "(ﾒ` ﾛ ´)",
    "Σ(▼□▼メ)", "(҂ `з´ )", "٩(╬ʘ益ʘ╬)۶", "↑_(ΦwΦ)Ψ", "(ﾉಥ益ಥ)ﾉ", "(＃＞＜)",
    "(；￣Д￣)", "(￢_￢;)", "(＾＾＃)", "(￣︿￣)", "ヾ( ￣O￣)ツ", "(ᗒᗣᗕ)՞",
    "(ノ_<。)ヾ(´ ▽ ` )", "ヽ(￣ω￣(。。 )ゝ", "(ﾉ_；)ヾ(´ ∀ ` )", "(´-ω-`( _ _ )",
    "(⌒_⌒;)", "(*/_＼)", "( ◡‿◡ *)", "(//ω//)", "(￣▽￣*)ゞ", "(„ಡωಡ„)",
    "(ﾉ´ з `)ノ", "(♡-_-♡)", "(─‿‿─)♡", "(´ ω `♡)", "(ღ˘⌣˘ღ)", "(´• ω •`) ♡",
    "╰(*´︶`*)╯♡", "(≧◡≦) ♡", "♡ (˘▽˘>ԅ( ˘⌣˘)", "σ(≧ε≦σ) ♡", "(˘∀˘)/(μ‿μ) ❤",
    "Σ>―(〃°ω°〃)♡→", "(* ^ ω ^)", "(o^▽^o)", "ヽ(・∀・)ﾉ", "(o･ω･o)", "(^人^)",
    "( ´ ω ` )", "(´• ω •`)", "╰(▔∀▔)╯", "(✯◡✯)", "(⌒‿⌒)", "(*°▽°*)",
    "(´｡• ᵕ •｡`)", "ヽ(>∀<☆)ノ", "＼(￣▽￣)／", "(o˘◡˘o)", "(╯✧▽✧)╯", "( ‾́ ◡ ‾́ )",
    "(๑˘︶˘๑)", "(´･ᴗ･ ` )", "( ͡° ʖ̯ ͡°)", "( ఠ ͟ʖ ఠ)", "( ಥ ʖ̯ ಥ)", "(≖ ͜ʖ≖)",
    "ヘ(￣ω￣ヘ)", "(ﾉ≧∀≦)ﾉ", "└(￣-￣└))", "┌(＾＾)┘", "(^_^♪)", "(〜￣△￣)〜",
    "(｢• ω •)｢", "( ˘ ɜ˘) ♬♪♫", "( o˘◡˘o) ┌iii┐", "♨o(>_<)o♨",
    "( ・・)つ―{}@{}@{}-", "(*´з`)口ﾟ｡ﾟ口(・∀・ )", "( *^^)o∀*∀o(^^* )", "-●●●-ｃ(・・ )",
    "(ﾉ≧∀≦)ﾉ ‥…━━━★", "╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ", "(∩ᄑ_ᄑ)⊃━☆ﾟ*･｡*･:≡( ε:)"
]

@bot.on_message(filters.command("react",config.COMMANDS))
def reaction (_, message):
    if message.reply_to_message:
         return message.reply_to_message.reply_text(random.choice(reactions))  
    else:
         message.reply_text(random.choice(reactions))

@bot.on_message(filters.command(["aq","animequotes"],config.COMMANDS))
def animequotes(_, message):
      message.reply_photo(random.choice(QUOTES_IMG))
