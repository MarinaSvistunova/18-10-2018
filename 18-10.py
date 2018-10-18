def main(*lst):
  return sorted(lst)


print(main((1, 8, 2, 99, 1.3, 5)))

if __name__ == '__main__':
  assert main(1, 8, 2, 99, 1.3, 5) == [1, 1.3, 2, 5, 8, 99],\
          "Сортировка по возрастанию"
