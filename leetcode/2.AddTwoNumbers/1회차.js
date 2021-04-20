/**
 * https://leetcode.com/problems/add-two-numbers/
 * 
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
 function ListNode(val, next) {
  this.val = (val === undefined ? 0 : val)
  this.next = (next === undefined ? null : next)
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  let carry = 0
  let head = null
  let cur = null
  let next = null
  while(carry || l1 || l2) {
    const { val: val1 } = l1 || { val: 0 }
    const { val: val2 } = l2 || { val: 0 }
    let val = val1 + val2 + carry
    carry = Number.parseInt(val / 10)
    if (carry) {
      val -= 10
    }
    if (cur === null) {
      cur = new ListNode(val, null)
      head = cur
    } else {
      next = new ListNode(val, null)
      cur.next = next
      cur = next
    }

    l1 = l1 && l1.next ? l1.next : undefined
    l2 = l2 && l2.next ? l2.next : undefined
  } 
  return head
};

const l1 = new ListNode(9, new ListNode(9, new ListNode(9, null))) 
const l2 = new ListNode(9, new ListNode(9, new ListNode(9, null))) 
addTwoNumbers(l1, l2)