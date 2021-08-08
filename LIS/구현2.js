function ListNode(val, right, left) {
    this.val = val === undefined ? 0 : val;
    this.right = right === undefined ? null : right;
    this.left = left === undefined ? null : left;
  }
  let head = null
  let pointer = null
  let trashBin = []
  const create = (n) => {
      let cur = null
      for(let i=0;i<n;i++) {
          const newNode = new ListNode(i, null, null)
          if (cur === null) {
              cur = newNode
              head = cur
              pointer = cur
          } else {
              cur.right = newNode
              newNode.left = cur
              cur = newNode
          }
      }
  }
  
  const moveLeft = (move) => {
      for (let i=0;i<move;i++) {
          pointer = pointer.left
      }
  }
  const moveRight(move) => {
      for (let i=0;i<move;i++) {
          pointer = pointer.right
      }
  }
  const remove = () => {
      let cur = null
      if (pointer.right === null) {
          cur = pointer.left
      } else {
          cur = pointer.right
      }
      trashBin.push(pointer.val)
      pointer.left = null
      pointer.right = null
      pointer = cur
  }
  const rollback = () => {
      let j = trashBin.shift()
      let p = null
      for (let i=0;i<j-1,i++) {
          p
      }
  }
  
  function solution(n, k, cmd) {
      
  }