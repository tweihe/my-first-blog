# -*- coding: utf-8 -*-
def categories_processor(request):
    length = request.POST.get('length')
    complexity = request.POST.get('complexity')
    if length != None:
        lengthval = int(length)
        complexval = int(complexity)
        testatron = lengthval * complexval

        the_essay = [["<p style='text-indent: 40px'> When people read anything, there are many unspoken expectations that are built into what they are reading. ",1],["People assume that what they are reading pertains to the subject that the title of the text claims it to be about. ",4],["People assume that what they are reading is fact or fiction based on the genre of the text. ",4],["One of the seemingly most obvious expectations that people have is that what they are reading was created by a human. ",1],["Despite people’s expectations, as can be seen from this project, what you read might not always be directly created by a human. ",1],["</p><p style='text-indent: 40px'>",5],["Humans have probably had an interest in streamlining the creative process for as long as they’ve had an interest in creating. ",2],["Creators have found ways to aid the final step in their creative process, disseminating their work, through advances in transportation and telecommunication. ",5],["The printing press, typewriter, and word-processing software have all helped writers get their thoughts into more permanent forms. ",5],["Libraries, along with a multitude of online search tools, have allowed writers to find information to use in the creation of their works. ",5],["Given all the advances in creation-streamlining technology over the centuries, the amount of effort (and where that effort is directed) that humans expend in fields like writing has changed dramatically. ",3],["How long could it be until humans are streamlined entirely out of the creative process themselves? ",2],["</p><p style='text-indent: 40px'>",2],["In some cases, this is already a reality. ",2],["In certain fields, normal, human-readable paragraphs of writing can already be written automatically with just the most basic information. ",3],["An article written by Metro discusses several areas where this is already occurring: The Associated Press already uses programs to generate financial reports, and some businesses already use automatic writing programs to create crossword puzzles, poetry, and in some instances, entire books. ",4],["Although the program that created this essay is more of a parlour trick or a prop for an elaborate thought experiment than an actual automatic essay writer, the framework to create something like this actually exists. ",1],["The implications of such a technology are wide-ranging and extremely important for society to explore further. ",1],["</p><p style='text-indent: 40px'>",4],["One issue related to this technology that will need to be addressed is that of ownership: Who would be considered the creator and owner of an automatically generated text? ",2],["The answer of who would be considered the creator of an automatically generated text probably depends largely on the process of generation of the text. ",2],["Theoretically, the user of the program, the creator of the program, the creator of the source material (if it exists), and the program itself all have some claim of having created the text, depending on the creation process. ",3],["For starters, who would be considered the creator of the essay you’re reading right now? ",3],["You, the user, gave this program the exact combination of configurations needed to create this essay, but the current form of the program only allows for the creation of 15 different essays, which were generated in a deterministic manner. (which means that the program will return the same essays given the same values) ",3],["If someone else were to stumble upon this same combination of configurations to create this essay, which is relatively likely, would they also be considered the creator? ",3],["This question can partially be answered by the Library of Babel. ",4],["The Library of Babel is a website created by Jonathan Basile, whose goal is to catalogue all combinations of characters of the English alphabet up to a certain length in characters. ",4],["The library is large enough now that one could already find any page of any average-sized book (with normal-sized typeface, in contemporary English) which has ever been created, and perhaps more interestingly, the page of any book that will ever be created. (with the same qualifiers) ",4],["In a similar sense to the experience of this program, the user can make a number of finite decisions that will lead them to a very specific configuration of information. (a page in the library) ",4],["Can a user take credit for this page, even though it has already been written? ",4],["One could argue that they could, because the chances of the generator of the text knowing about this specific page are very slim. (easily less than one in a billion) ",5],["This is in stark contrast to the mechanics of this program, in which there is a one in 15 chance of stumbling upon this exact essay. ",5],["It could be said that as the likelihood of the essay being generated goes down in a system where the user has control of the configuration, the credit that the user gets for the configuration increases. ",5],["Due to all of the different facters at play with a program like this, this is definitely a complicated issue! ",2],["</p><p style='text-indent: 40px'>",3],["In the future, this technology will only become more prevalent and sophisticated. ",1],["Already, services such as SMMRY, which can automatically create a summary of a larger text based on the frequency of keywords, and Google Translate, which is tasked with writing its own interpretation of a text in a different language, blur the lines between human writing and machine writing. ",3],["The demand for more fully automated writing services will be tremendous as well: Imagine what desperate students might do with a fully realized version of this program. ",2],["According to an article by Thomas Bartlett, the demand for the services of so-called essay mills hasn’t gone anywhere but up. ",5],["This demand will likely feed seamlessly into automated writing demand. ",5],["Mentioned in the article, though, was the fact that some students actually use these essays from essay mills to serve as inspiration for their own essays. ",5],["Perhaps the future of automated writing, then, could be more optimistic. ",5],["Essay-writing programs could be used to push the creative boundaries of students. ",5],["Whatever the future holds, this peculiar phenomenon of a digital text generating another digital text has the potential to change the way we think about creativity and writing. </p>",1]]
        essaytest = ""
        for i in the_essay:
            if i[1] <= lengthval:
                essaytest = essaytest + i[0]

        return {'length': length, 'complexity' : complexity, 'testatron': testatron, 'essaytest': essaytest}

    return {'length': length, 'complexity' : complexity}
