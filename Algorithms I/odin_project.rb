# frozen_string_literal: true

def fibs(num)
  res = [0, 1]
  num -= 2

  fibs_rec(num, res)
end

def fibs_rec(num, res)
  res << res[res.length - 1] + res[res.length - 2]

  return fibs_rec(num - 1, res) if num > 1

  res
end

def merge_sort(array)
  return array if array.length <= 1

  m = (array.length / 2).round
  first = array.take(m)
  last = array.drop(m)
  sorted_first = merge_sort(first)
  sorted_last = merge_sort(last)
  merge(sorted_first, sorted_last)
end

def merge(left, right)
  return left if right.empty?
  return right if left.empty?

  small = if left.first <= right.first
            left.shift
          else
            right.shift
          end

  recurse = merge(left, right)

  [small].concat(recurse)
end

p merge_sort([12, 11, 13, 5, 6, 7])
