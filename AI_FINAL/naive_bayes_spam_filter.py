train_spam = ['send us your password', 'review our website', 'send your password', 'send us your account']
train_ham = ['Your activity report','benefits physical activity', 'the importance vows']
test_emails = {'spam':['renew your password', 'renew your vows'], 'ham':['benefits of our account', 'the importance of physical activity']}
vocab_words_spam = []

for sentence in train_spam:
    sentence_as_list = sentence.split()
    for word in sentence_as_list:
        vocab_words_spam.append(word)

print(vocab_words_spam)

vocab_unique_words_spam = list(dict.fromkeys(vocab_words_spam))
print(vocab_unique_words_spam)

dict_spamicity = {}
for w in vocab_unique_words_spam:
    emails_with_w = 0  # counter
    for sentence in train_spam:
        if w in sentence:
            emails_with_w += 1

    print(f"Number of spam emails with the word {w}: {emails_with_w}")
    total_spam = len(train_spam)
    spamicity = (emails_with_w + 1) / (total_spam + 2)
    print(f"Spamicity of the word '{w}': {spamicity} \n")
    dict_spamicity[w.lower()] = spamicity
print(dict_spamicity)