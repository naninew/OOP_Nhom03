import Query_Builder.*;
import Query_Builder.Card;
import Query_Builder.Deck;
import py4j.GatewayServer;
public class Main {
    Card card=new Card("card");
    Card_tag card_tag=new Card_tag("card_tag");
    Deck deck=new Deck("deck");
    Deck_setting deck_setting=new Deck_setting("deck_setting");
    Deck_Tag deck_tag=new Deck_Tag("deck_tag");
    Learning_progress learning_progress=new Learning_progress("learning_progress");
    User_account user_account=new User_account("user_account");
    Query query=new Query("");
    Condition condition=new Condition("");
    Operator operator=new Operator("");
    String placeholder="{}";

    public String SayHello(){
        return "This String is from Java";
    }
    public String get_UserPassword(){
        return query.select(user_account.password)
                .from(user_account)
                .where(condition.whereCondition(user_account.email,operator.Equal(),placeholder)).toString();
    }
    public String get_UserId(){
        return query.select(user_account.user_id.toString())
                .from(user_account)
                .where(condition.whereCondition(user_account.email,operator.Equal(),placeholder)).toString();
    }
    public String get_AuthorName(){
        return query.select(user_account.user_name)
                .from(user_account)
                .where(condition.whereCondition(user_account.user_id.toString(),operator.Equal(),placeholder)).toString();
    }
    public String get_DeckIdList(){
        return query.select(deck.deck_id.toString())
                .from(deck)
                .where(condition.multiCondition(
                        condition.whereCondition(deck.author_id.toString(),operator.Equal(),placeholder),
                        operator.Or(),
                        condition.whereCondition(deck.isPublic,operator.Equal(),"true"))).toString();
    }
    public String get_CardIdList(){
        return query.select(card.card_id.toString())
                .from(card).where(condition.whereCondition(card.deck_id.toString(),operator.Equal(),placeholder)).toString();
    }

    public static void main(String[] args) {
        GatewayServer gatewayServer =new GatewayServer(new Main(),25333);
        gatewayServer.start();
        System.out.println("Gateway Server Started");
        Main main=new Main();
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.get_UserPassword());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.get_UserId());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.get_AuthorName());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.get_DeckIdList());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.get_CardIdList());
        System.out.println("- - - - - - - - - - - - - - - - - - -");

        System.out.println(main.card.getDetailByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.card.updateDetailByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.card.deleteByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.card.insertDetail());

        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.card_tag.getDetailByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.card_tag.updateDetailByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.card_tag.deleteByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.card_tag.insertDetail());

        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.deck.getDetailByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.deck.updateDetailByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.deck.deleteByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.deck.insertDetail());

        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.deck_setting.getDetailByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.deck_setting.updateDetailByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.deck_setting.deleteByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.deck_setting.insertDetail());

        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.deck_tag.getDetailByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.deck_tag.updateDetailByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.deck_tag.deleteByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.deck_tag.insertDetail());

        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.learning_progress.getDetailByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.learning_progress.updateDetailByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.learning_progress.deleteByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.learning_progress.insertDetail());

        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.user_account.getDetailByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.user_account.updateDetailByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.user_account.deleteByKey());
        System.out.println("- - - - - - - - - - - - - - - - - - -");
        System.out.println(main.user_account.insertDetail());

        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(main);
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(main);
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(main);
//        System.out.println("- - - - - - - - - - - - - - - - - - -");




    }
}


//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(card.updateRow());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(card_tag.updateRow());
//        QueryService QS=new QueryService();
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getUserAccountUserNameQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getCardBasicInfoByIdQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getCardAllCardsByUserThroughDeckQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getDeckBasicInfoByIdQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getCardCardIdsByDeckIdQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getCardCountCardsInDeckQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getCardQueryGeneratorInstance());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getDeckAvailableDeckIdsForUserQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getDeckDecksByAuthorQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getDeckBasicInfoByIdQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getDeckSettingCardsPerDayQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getDeckNameAndLanguageByIdQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getLearningProgressCardsToReviewNext7DaysQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getCardBasicInfoByIdQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getCardCardIdsByDeckIdQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getCardSelectAllQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getLearningProgressCardsToReviewTodayQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getUserAccountThemeQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getUserAccountThemeQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getUserAccountUpdateQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getDeckSettingDeleteByCompositeIdQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getDeckBasicInfoByIdQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getUserAccountPasswordQuery());
//        System.out.println("- - - - - - - - - - - - - - - - - - -");
//        System.out.println(QS.getUserAccountDeleteByIdQuery());