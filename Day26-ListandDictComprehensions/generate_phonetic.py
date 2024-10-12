def generate_phonetic(df):
    # get input from user
    name = input('Enter a name: ').upper().replace(' ', '')

    try:
        list_ch = list(name)  # split string into characters, ignore space character

        # create a list of codes matching characters in input string
        result = [df.query('letter == @ch').code.to_string(index=False, header=False)
                  if not df.query('letter == @ch').empty
                  else None
                  for ch in list_ch]

        if None in result:
            print('Only alphabetical characters in name please.')
            generate_phonetic(df)
        else:
            print(result)

    except ValueError as e:
        print(e)