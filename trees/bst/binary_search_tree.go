/**
 * Binary Search Tree
 * BST with simple operatiins
 * Insert | Delete | Find
 */

package main

import (
	"errors"
	"fmt"
)

//Node is the tree node type
type Node struct {
	Left  *Node
	Right *Node
	Val   int32
}

//Tree data structure
type Tree struct {
	Root *Node
}

func (n *Node) insert(val int32) error {
	if n == nil {
		return errors.New("nil tree")
	}

	switch {
	case val == n.Val:
		return nil
	case val < n.Val:
		if n.Left == nil {
			n.Left = &Node{nil, nil, val}
			return nil
		}
		n.Left.insert(val)
	case val > n.Val:
		if n.Right == nil {
			n.Right = &Node{nil, nil, val}
			return nil
		}
		n.Right.insert(val)
	}
	return nil
}

func (n *Node) find(val int32) bool {
	if n == nil {
		return false
	}
	switch {
	case n.Val == val:
		return true
	case val < n.Val:
		return n.Left.find(val)
	case n.Val < val:
		return n.Right.find(val)
	}
	return false
}

func (n *Node) deleteNode(parent *Node, replacement *Node) error {
	if n == nil {
		return errors.New("empty node")
	}
	if parent.Left == n {
		parent.Left = replacement
		return nil
	}
	if parent.Right == n {
		parent.Right = replacement
		return nil
	}
	return nil
}

func (n *Node) delete(parent *Node, val int32) error {
	if n == nil {
		return errors.New("empty node")
	}
	switch {
	case n.Val < val:
		return n.Right.delete(n, val)
	case val < n.Val:
		return n.Left.delete(n, val)
	default:
		if n.Left == nil && n.Right == nil {
			n.deleteNode(parent, nil)
			return nil
		}
		if n.Left == nil {
			n.deleteNode(parent, n.Right)
			return nil
		}
		if n.Right == nil {
			n.deleteNode(parent, n.Left)
			return nil
		}
		rep, repParent := n.Left.findMax(n)
		n.Val = rep.Val
		return rep.delete(repParent, rep.Val)
	}
}

func (t *Tree) deleteInTree(val int32) (bool, error) {
	if t.Root == nil {
		return false, errors.New("empty tree")
	}

	err := t.Root.delete(nil, val)
	if err != nil {
		return false, err
	}
	return false, nil
}

func (n *Node) findMax(parent *Node) (*Node, *Node) {
	if n == nil {
		return nil, nil
	}
	if n.Right == nil {
		return n, parent
	}
	return n.Right.findMax(n)
}

func (t *Tree) find(val int32) (bool, error) {
	if t == nil {
		return false, errors.New("empty tree")
	}
	return t.Root.find(val), nil
}

//create a new tree or insert an element into tree
func (t *Tree) insert(val int32) error {
	if t.Root == nil {
		t.Root = &Node{Left: nil, Right: nil, Val: val}
		return nil
	}
	return t.Root.insert(val)
}

func (t *Tree) traverse() error {
	if t.Root == nil {
		return errors.New("empty")
	}
	t.Root.traverse()
	return nil
}

func (n *Node) traverse() {
	if n == nil {
		return
	}
	n.Left.traverse()
	fmt.Printf("%d", n.Val)
	n.Right.traverse()
}

func main() {
	t := &Tree{&Node{nil, nil, 5}}
	t.insert(2)
	t.insert(4)
	t.insert(3)
	t.insert(1)
	t.insert(7)
	t.insert(6)
	t.insert(9)
	t.insert(8)
	t.traverse()
	fmt.Println()
	t.deleteInTree(7)
	t.traverse()
	fmt.Println()
	t.deleteInTree(5)
	t.traverse()
}
