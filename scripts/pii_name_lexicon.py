"""Given names and surnames for positive person-name detection in OCR text.

The scanner flags capitalized tokens only when they match this lexicon (plus
style-guide example allowlists), rather than treating every Title Case pair as
a person name.
"""

from __future__ import annotations


def _words(block: str) -> frozenset[str]:
    return frozenset(word.strip().lower() for word in block.split() if word.strip())


# US Census / SSA frequent given names + Braze style-guide unisex examples.
GIVEN_NAMES = _words(
    """
    aaron abigail adam adrian alan albert alex alexander alexis alice alicia alison
    allen amanda amber amy ana andrea andrew angela ann anna anne anthony antonio
    ashley audrey austin barbara benjamin bernard betty beverly billy bobby brad
    bradley brandon brenda brett brian brittany bruce bryan caleb cameron carl
    carlos carol caroline carolyn carrie casey catherine cecilia charles charlotte cheryl
    chris christian christina christine christopher cindy claire clarence claude
    clayton clifford clyde cole colin connor corey craig crystal cynthia daisy
    dale dan daniel danielle danny darlene darren dave david dawn dean debbie
    deborah debra denise dennis derek diana diane dolores don donald donna dora
    dorothy douglas drew dylan ed edgar edith edward edwin eileen elaine eleanor
    elizabeth ella ellen elmer emily emma eric erica erin ernest esther ethan
    eugene evan evelyn faith felicia fiona flora florence france francis frank
    franklin fred gabriel gail garrett gary gavin gene george gerald gina gloria
    grace grant greg gregory hailey harold harry harvey hayden heather helen
    henry holly howard hunter ian irene isaac jack jackie jacob jade jake james
    jamie jane janet janice jared jasmine jason jean jeff jeffrey jen jennifer
    jenny jeremy jerry jesse jessica jill jim jimmy jo joan joe joel john johnny
    jon jonathan jordan jorge jose joseph josh joshua joy joyce juan judith judy
    julia julie julius justin karen kate katherine kathleen kathryn kathy katie
    kay keith kelly ken kenneth kenny kevin kim kimberly kyle lana lance larry
    laura lauren lawrence lee leo leon leonard leslie lester lewis lily linda
    lisa lloyd logan lois lori lou louis louise lucas lucille lucy luis luke
    lynn madison mandy margaret maria marie marilyn marion mark martha martin
    mary mason mathew matthew maureen max megan melissa michelle miguel mike
    mildred misty molly monica morgan nancy natalie nathan neil nelson nicholas
    nick nicole nina noah norma norman olivia oscar owen pam pamela pat patricia
    patrick paul paula peggy penny pete peter phil philip phillip phyllis rachel
    ralph randy ray raymond rebecca regina renee rex rhonda ricardo richard rick
    ricky riley rita rob robert robin roger ron ronald rosa rose ross roy ruby
    russ russell ruth ryan sally sam samantha samuel sandra sara sarah scott sean
    shannon sharon shawn sheila shelley sherri shirley sidney simon skylar sophia
    spencer stacey stan stanley stella stephanie stephen steve steven sue susan
    sydney sylvia tammy tanya tara taylor ted teresa terri terry thelma theresa
    thomas tiffany tim timothy tina todd tom tommy toni tony tracy travis trevor
    troy tyler valerie vanessa veronica victor vincent virginia wade walter wanda
    wayne wendy wesley will william willie yuri zach zachary zoe
    """
)

# Frequent English surnames (used for Name_Last column singles and pair validation).
SURNAMES = _words(
    """
    adams alexander allen anderson bailey baker barnes bell bennett brooks brown
    butler campbell carter clark collins cook cooper cox crawford diaz edwards
    elliott evans fisher flores ford foster garcia gonzalez graham gray green
    griffin hall hamilton harris hayes henderson henry hill howard hughes jackson
    james jenkins johnson johnston jones kelly kennedy king lee lewis long lopez
    marshall martin martinez miller mitchell moore morgan morris murphy nelson
    nguyen parker patel perez perry peterson phillips powell ramirez reed
    richardson riley rivera roberts robinson rodriguez rogers ross russell
    sanchez sanders scott simmons smith stewart taylor thomas thompson torres
    turner walker wallace ward watson white williams wilson wood wright young
    higgins kim chen wang li zhang singh khan ahmed
    """
)
