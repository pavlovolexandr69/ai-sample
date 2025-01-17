using System;
using Xunit;

public class LinkedTests
{
    [Fact]
    public void HasCycle_NullHead_ReturnsFalse()
    {
        var linked = new Linked();
        Assert.False(linked.HasCycle(null));
    }

    [Fact]
    public void HasCycle_SingleNode_ReturnsFalse()
    {
        var linked = new Linked();
        var node = new ListNode(1);
        Assert.False(linked.HasCycle(node));
    }

    [Fact]
    public void HasCycle_TwoNodesNoCycle_ReturnsFalse()
    {
        var linked = new Linked();
        var node1 = new ListNode(1);
        var node2 = new ListNode(2);
        node1.next = node2;
        Assert.False(linked.HasCycle(node1));
    }

    [Fact]
    public void HasCycle_CycleInTwoNodes_ReturnsTrue()
    {
        var linked = new Linked();
        var node1 = new ListNode(1);
        var node2 = new ListNode(2);
        node1.next = node2;
        node2.next = node1;
        Assert.True(linked.HasCycle(node1));
    }

    [Fact]
    public void HasCycle_LongListNoCycle_ReturnsFalse()
    {
        var linked = new Linked();
        var node1 = new ListNode(1);
        var node2 = new ListNode(2);
        var node3 = new ListNode(3);
        var node4 = new ListNode(4);
        node1.next = node2;
        node2.next = node3;
        node3.next = node4;
        Assert.False(linked.HasCycle(node1));
    }

    [Fact]
    public void HasCycle_CycleInMiddle_ReturnsTrue()
    {
        var linked = new Linked();
        var node1 = new ListNode(1);
        var node2 = new ListNode(2);
        var node3 = new ListNode(3);
        var node4 = new ListNode(4);
        node1.next = node2;
        node2.next = node3;
        node3.next = node4;
        node4.next = node2;
        Assert.True(linked.HasCycle(node1));
    }
}
