def main(*lst):
  return sorted(lst)

a = [int(i) for i in input().split()]
print(main(*a))

if __name__ == '__main__':
  assert main(1, 8, 2, 99, 1.3, 5) == [1, 1.3, 2, 5, 8, 99],\
          "Сортировка по возрастанию"
