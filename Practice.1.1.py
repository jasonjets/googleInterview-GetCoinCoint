           ### Setup info
campaign_name = input("What is the campaign name? ")
pair = input("What is the pair in focus? ")
trading_opportunity_feedback = input(f"""How many trading opportunities
will there be this week on {pair}

"1" = Not many
"2" = Many
"3" = Slim to nothing
--->""")
headline_result = input("""Enter a digit for one of the following headlines...
H(1) “They didn’t think I could, _______, but I did.” 
H(2) “Who else wants _________”
H(3) “How _________ made me __________”
H(4) “Are you __________?”
H(5) “How I ______________”
H(6) “Secrets of ____________”
H(7) “Thousands/millions ets. Now ____________ even though they ____________”
H(8) “Warning: ____________”
H(9) “Give me ____________ and I’ll ____________”
H(10) “____________ ways to ____________”
--->""")
attention_grabber = input(f"What's the most exciting thing happening with {pair} ")
            ### Lists
trading_opportunity_list ={
1: "won't have many opportunities" ,
2: "will provide many opportunities" ,
3: "may be flat"} #Fill these on a scale of 1 to 10
headline_list = {
1: "They didn’t think I could, _______, but I did." ,
2: "Who else wants ________" ,
3: "How _________ made me ________" ,
4: "Are you __________?" ,
5: "How I ______________"  ,
6: "Secrets of ____________" ,
7: "Thousands/millions ets. Now ____________ even though they ____________" ,
8: "Warning: ____________" ,
9: "Give me ____________ and I’ll ____________" ,
10: "____________ ways to ____________" ,}
selected_headline = (headline_list[int(headline_result)])
if int(headline_result) == 1:
    input("They didn't think I could ")
    input("until I")
if int(headline_result) == 2:
    print("it works")
print(f"""
Headline: {headline_list[int(headline_result)]}
This week, {pair.upper()} {trading_opportunity_list[int(trading_opportunity_feedback)]} considering {attention_grabber}

""")