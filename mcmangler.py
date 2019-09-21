import argparse
import itertools

suffixes = ["2018", "2018!", "2019", "2019!", "1", "!1", "1!", "12", "12!", "123", "123!", "!123"]

def main():
  args = input_handler()

  if args.word:
    mcmangle(args.word.lower())
  elif args.file:
    try:
      f = open(args.file)
    except:
      print("couldn't read file")

    for line in f:
        mcmangle(line.strip().lower())
  else:
    print("hi")


def mcmangle(word):
  rules_root = build_rules_root(word)
  rules_combination = build_rules_combination(rules_root)

  for rule_set in rules_combination:
    transformed = run_rule_set(word, rule_set)

    print(transformed)
    print(transformed.upper())
    if transformed[0].isalpha():
      print(transformed.capitalize())

    for suffix in suffixes:
      print(transformed + suffix)
      print(transformed.upper() + suffix)
      if transformed[0].isalpha():
        print(transformed.capitalize() + suffix)


def run_rule_set(word, rule_set):
  transformed = word

  for rule in rule_set:
    occurence = int(rule[1])
    char_to_replace = rule[2]
    char_to_insert = rule[9] 

    index_in_word = find_nth(word, char_to_replace, occurence)
    transformed = transformed[:index_in_word] + char_to_insert + transformed[index_in_word+1:]

  return transformed


def build_rules_combination(rules_root):
  rules_root_combination = [()]

  for i in range(1, len(rules_root)+1):
    rules_root_combination = rules_root_combination + list(itertools.combinations(rules_root, i))

  return rules_root_combination


def build_rules_root(word):
  rules_root = []

  a_ct = 0
  i_ct = 0
  s_ct = 0
  e_ct = 0
  o_ct = 0

  #speaks https://hashcat.net/wiki/doku.php?id=rule_based_attack#using_p_nth_instance_of_a_character_with_positional_rules
  for letter in list(word):
    if letter == 'a':
      a_ct = a_ct + 1
      rules_root.append("%" + str(a_ct) + letter + " Dp ip@")
    elif letter == 'i':
      i_ct = i_ct + 1
      rules_root.append("%" + str(i_ct) + letter + " Dp ip1")
    elif letter == 's':
      s_ct = s_ct + 1
      rules_root.append("%" + str(s_ct) + letter + " Dp ip$")
    elif letter == 'e':
      e_ct = e_ct + 1
      rules_root.append("%" + str(e_ct) + letter + " Dp ip3")
    elif letter == 'o':
      o_ct = o_ct + 1
      rules_root.append("%" + str(o_ct) + letter + " Dp ip0")

  return rules_root


#https://stackoverflow.com/questions/1883980/find-the-nth-occurrence-of-substring-in-a-string
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n = n - 1
    return start


def input_handler():
  desc = """Generate l33tspeak combinations for password brute forcing.

            Quick examples:
            ./mcmangler.py -w Microsoft 
            ./mcmangler.py -f words.txt"""

  p = argparse.ArgumentParser(description=desc, formatter_class=argparse.RawTextHelpFormatter)
  p.add_argument('--word', 
                  '-w', 
                  help='a word to mangle')
  p.add_argument('--file', 
                  '-f',
                  help='newline separated file with a bunch of words to mangle')

  args = p.parse_args()
  return args


main()