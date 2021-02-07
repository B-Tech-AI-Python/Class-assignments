import textwrap

paragraph = """Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph. A paragraph is defined as “a group of sentences or a single sentence that forms a unit” (Lunsford and Connors 116). Length and appearance do not determine whether a section in a paper is a paragraph. For instance, in some styles of writing, particularly journalistic styles, a paragraph can be just one sentence long. Ultimately, a paragraph is a sentence or group of sentences that support one main idea. In this handout, we will refer to this as the “controlling idea,” because it controls what happens in the rest of the paragraph. What is the most important idea that you are trying to convey to your reader? The information in each paragraph must be related to that idea. In other words, your paragraphs should remind your reader that there is a recurrent relationship between your thesis and the information in each paragraph. A working thesis functions like a seed from which your paper, and your ideas, will grow. The whole process is an organic one—a natural progression from a seed to a full-blown paper where there are direct, familial relationships between all of the ideas in the paper."""

paragraph = textwrap.fill(paragraph)

print()
print("LOWERCASE PARAGRAPH")
print(paragraph.lower())

print()
print("WORD COUNT FOR PARAGRAPH")
print(len(paragraph.split(' ')))

print()
print("CHARACTER COUNT FOR PARAGRAPH")
print(len(paragraph))

print()
print("REMOVING WORDS FROM PARAGRAPH")

words = ['the', 'a', 'an', 'are', 'in', 'on', 'with', 'and']

new_para = [word for word in paragraph.split() if word.lower() not in words]
new_para = ' '.join(new_para)

new_para = textwrap.fill(new_para)
print(new_para)

print()
print("WORD COUNT FOR NEW PARAGRAPH")
print(len(new_para.split(' ')))

print()
print("CHARACTER COUNT FOR NEW PARAGRAPH")
print(len(new_para))

print()
print("COUNTING DUPLICATES IN TEXT")


def wordCount(string):
    theWordCount = dict()
    theWords = string.split()

    for word in theWords:
        if word in theWordCount:
            theWordCount[word] += 1
        else:
            theWordCount[word] = 1

    return theWordCount


original_count = wordCount(paragraph)
new_count = wordCount(new_para)

print("Original para count:")
print(original_count)

print("\nRemoved words para count:")
print(new_count)
