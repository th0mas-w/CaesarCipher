def caesarCipher(query,shift):
    query,result,abc = list(query),[],['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for x in range(len(query)):
          if query[x] in abc:
              result.append(abc[abc.index(query[x]) + shift])
          else:
              result.append(query[x])
    return "".join(result)
print(caesarCipher(input("Enter your plain text string: ").lower(),int(input("How many letters do you want to shift by: "))))
