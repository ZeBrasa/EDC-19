$(document).ready(function() {
	$("#btnAdd").click(function() {
		var num     = $(".clonedSection").length;
		var newNum  = new Number(num + 1);

		var newSection = $("#clonedSection" + num).clone().attr("id", "clonedSection" + newNum);

		newSection.children(":first").children(":first").attr("id", "name" + newNum).attr("name", "name" + newNum);
		newSection.children(":nth-child(3)").children(":first").attr("id", "desc" + newNum).attr("name", "desc" + newNum);
		newSection.children(":nth-child(4)").children(":first").attr("id", "brand" + newNum).attr("name", "brand" + newNum);
		newSection.children(":nth-child(5)").children(":first").attr("id", "code" + newNum).attr("name", "code" + newNum);
		newSection.children(":nth-child(6)").children(":first").attr("id", "coop" + newNum).attr("name", "coop" + newNum);
		newSection.children(":nth-child(7)").children(":first").attr("id", "yes" + newNum).attr("name", "yes" + newNum);
		newSection.children(":nth-child(7)").children(":nth-child(2)").attr("id", "no" + newNum).attr("name", "no" + newNum);
		newSection.children(":nth-child(8)").children(":first").attr("id", "comm" + newNum).attr("name", "comm" + newNum);

		$(".clonedSection").last().append(newSection)

		$("#btnDel").attr("disabled","");

		if (newNum == 5)
			$("#btnAdd").attr("disabled","disabled");
	});

	$("#btnDel").click(function() {
		var num = $(".clonedSection").length; // how many "duplicatable" input fields we currently have
		$("#clonedSection" + num).remove();     // remove the last element

		// enable the "add" button
		$("#btnAdd").attr("disabled","");

		// if only one element remains, disable the "remove" button
		if (num-1 == 1)
			$("#btnDel").attr("disabled","disabled");
	});

	$("#btnDel").attr("disabled","disabled");
});