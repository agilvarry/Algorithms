# frozen_string_literal: false

# linked list
class LinkedList
  def initialize(value = nil)
    @head = Node.new(value)
  end

  attr_reader :head

  def append(value, node = @head)
    if node.next.nil?
      node.next = Node.new(value)
    else
      append(value, node.next)
    end
  end

  def prepend(value)
    head = Node.new(value, @head)
    @head = head
  end

  def size
    size_rec(@head, 1)
  end

  def tail
    tail_rec(@head)
  end

  def at(index)
    find_index(@head, index - 1)
  end

  def pop(node = @head)
    if node.next.next.nil?
      node.next = nil
    else
      pop(node.next)
    end
  end

  def contains?(value, node = @head)
    return true if node.value == value
    return false if node.next.nil?

    contains?(value, node.next)
  end

  def find(value, node = @head, idx = 0)
    return idx if node.value == value
    return nil if node.next.nil?

    find(value, node.next, idx + 1)
  end

  def to_s(node = @head, str = "")
    str << "( #{node.value} ) -> "
    return str << 'nil' if node.next.nil?

    
    to_s(node.next, str)
  end

  private

  def size_rec(node, num)
    return num if node.next.nil?

    size_rec(node.next, num + 1)
  end

  def tail_rec(node)
    return node if node.next.nil?

    tail_rec(node.next)
  end

  def find_index(node, idx)
    return node if idx <= 0

    find_index(node.next, idx - 1)
  end

  
end

# linked list nodes
class Node
  attr_accessor :value, :next

  def initialize(value = nil, next_node = nil)
    @value = value
    @next = next_node
  end
end

list = LinkedList.new
p list.to_s
