def main():
    import time
    from generate_phrase import generate_random_paragraph
    from wpm_calculator import Calculate

    pg_generator = generate_random_paragraph

    phrase = pg_generator(1)

    word_count = len(phrase.split())

    begin = input('Please type: ' + phrase + '\nPress enter once ready')

    t0 = time.time()
    attempt = input('\n')
    t1 = time.time()

    calculate = Calculate(t0, t1, word_count)
    wpm = calculate.get_wpm()

    if attempt == phrase:
        print('\nYour WPM ' + wpm)
    else:
        print('WPM: ' + wpm + '\nincorrect')


if __name__ == '__main__':
    main()
