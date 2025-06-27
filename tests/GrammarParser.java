// Generated from Grammar.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class GrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, SEMI=28, NL=29, NUM=30, FLOAT=31, BOOL=32, 
		StringLiteral=33, UnterminatedStringLiteral=34, NULL=35, BlockComment=36, 
		Comment=37, VARNAME=38, ADD=39, SUB=40, MUL=41, DIV=42, MOD=43;
	public static final int
		RULE_prog = 0, RULE_statement = 1, RULE_bracket_statement = 2, RULE_imp = 3, 
		RULE_var_declaration = 4, RULE_var = 5, RULE_for_loop = 6, RULE_conditional_statement = 7, 
		RULE_elif = 8, RULE_else = 9, RULE_truth = 10, RULE_function_def = 11, 
		RULE_varname_list = 12, RULE_var_list = 13, RULE_brackets = 14, RULE_expr = 15;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "statement", "bracket_statement", "imp", "var_declaration", "var", 
			"for_loop", "conditional_statement", "elif", "else", "truth", "function_def", 
			"varname_list", "var_list", "brackets", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'.'", "'import'", "'public'", "'='", "'['", "']'", "'!'", "'for'", 
			"'('", "'in'", "')'", "'{'", "'}'", "'if'", "'while'", "'elif'", "'else'", 
			"'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'def'", 
			"','", null, null, null, null, null, null, null, "'null'", null, null, 
			null, "'+'", "'-'", "'*'", "'/'", "'%'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, "SEMI", "NL", "NUM", "FLOAT", "BOOL", "StringLiteral", 
			"UnterminatedStringLiteral", "NULL", "BlockComment", "Comment", "VARNAME", 
			"ADD", "SUB", "MUL", "DIV", "MOD"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Grammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public GrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public List<TerminalNode> SEMI() { return getTokens(GrammarParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(GrammarParser.SEMI, i);
		}
		public List<Bracket_statementContext> bracket_statement() {
			return getRuleContexts(Bracket_statementContext.class);
		}
		public Bracket_statementContext bracket_statement(int i) {
			return getRuleContext(Bracket_statementContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public List<ImpContext> imp() {
			return getRuleContexts(ImpContext.class);
		}
		public ImpContext imp(int i) {
			return getRuleContext(ImpContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(39);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
					case 1:
						{
						setState(34);
						_errHandler.sync(this);
						switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
						case 1:
							{
							setState(32);
							statement();
							}
							break;
						case 2:
							{
							setState(33);
							imp();
							}
							break;
						}
						setState(36);
						match(SEMI);
						}
						break;
					case 2:
						{
						setState(38);
						bracket_statement();
						}
						break;
					}
					} 
				}
				setState(43);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NormalStatementContext extends StatementContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Var_declarationContext var_declaration() {
			return getRuleContext(Var_declarationContext.class,0);
		}
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public NormalStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FileStatementContext extends StatementContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Var_declarationContext var_declaration() {
			return getRuleContext(Var_declarationContext.class,0);
		}
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public List<TerminalNode> VARNAME() { return getTokens(GrammarParser.VARNAME); }
		public TerminalNode VARNAME(int i) {
			return getToken(GrammarParser.VARNAME, i);
		}
		public FileStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			int _alt;
			setState(61);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				_localctx = new NormalStatementContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(47);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
				case 1:
					{
					setState(44);
					expr(0);
					}
					break;
				case 2:
					{
					setState(45);
					var_declaration();
					}
					break;
				case 3:
					{
					setState(46);
					var();
					}
					break;
				}
				}
				break;
			case 2:
				_localctx = new FileStatementContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(53);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(49);
						match(VARNAME);
						setState(50);
						match(T__0);
						}
						} 
					}
					setState(55);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
				}
				setState(59);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
				case 1:
					{
					setState(56);
					expr(0);
					}
					break;
				case 2:
					{
					setState(57);
					var_declaration();
					}
					break;
				case 3:
					{
					setState(58);
					var();
					}
					break;
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Bracket_statementContext extends ParserRuleContext {
		public Conditional_statementContext conditional_statement() {
			return getRuleContext(Conditional_statementContext.class,0);
		}
		public Function_defContext function_def() {
			return getRuleContext(Function_defContext.class,0);
		}
		public For_loopContext for_loop() {
			return getRuleContext(For_loopContext.class,0);
		}
		public Bracket_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bracket_statement; }
	}

	public final Bracket_statementContext bracket_statement() throws RecognitionException {
		Bracket_statementContext _localctx = new Bracket_statementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_bracket_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__13:
			case T__14:
				{
				setState(63);
				conditional_statement();
				}
				break;
			case T__2:
			case T__25:
				{
				setState(64);
				function_def();
				}
				break;
			case T__7:
				{
				setState(65);
				for_loop();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ImpContext extends ParserRuleContext {
		public List<TerminalNode> VARNAME() { return getTokens(GrammarParser.VARNAME); }
		public TerminalNode VARNAME(int i) {
			return getToken(GrammarParser.VARNAME, i);
		}
		public ImpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_imp; }
	}

	public final ImpContext imp() throws RecognitionException {
		ImpContext _localctx = new ImpContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_imp);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(T__1);
			setState(73);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(69);
					match(VARNAME);
					setState(70);
					matchWildcard();
					}
					} 
				}
				setState(75);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			setState(76);
			match(VARNAME);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Var_declarationContext extends ParserRuleContext {
		public Var_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_declaration; }
	 
		public Var_declarationContext() { }
		public void copyFrom(Var_declarationContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ListVarContext extends Var_declarationContext {
		public Token name;
		public Var_listContext vals;
		public TerminalNode VARNAME() { return getToken(GrammarParser.VARNAME, 0); }
		public Var_listContext var_list() {
			return getRuleContext(Var_listContext.class,0);
		}
		public ListVarContext(Var_declarationContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SingleVarContext extends Var_declarationContext {
		public Token name;
		public StatementContext exp;
		public TerminalNode VARNAME() { return getToken(GrammarParser.VARNAME, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public SingleVarContext(Var_declarationContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MultiVarContext extends Var_declarationContext {
		public Varname_listContext name;
		public Varname_listContext vals;
		public List<Varname_listContext> varname_list() {
			return getRuleContexts(Varname_listContext.class);
		}
		public Varname_listContext varname_list(int i) {
			return getRuleContext(Varname_listContext.class,i);
		}
		public MultiVarContext(Var_declarationContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ListSetContext extends Var_declarationContext {
		public Token name;
		public Token index;
		public StatementContext exp;
		public TerminalNode VARNAME() { return getToken(GrammarParser.VARNAME, 0); }
		public TerminalNode NUM() { return getToken(GrammarParser.NUM, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public ListSetContext(Var_declarationContext ctx) { copyFrom(ctx); }
	}

	public final Var_declarationContext var_declaration() throws RecognitionException {
		Var_declarationContext _localctx = new Var_declarationContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_var_declaration);
		try {
			setState(113);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				_localctx = new SingleVarContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(80);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__2:
					{
					setState(78);
					match(T__2);
					}
					break;
				case VARNAME:
					{
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(82);
				((SingleVarContext)_localctx).name = match(VARNAME);
				setState(83);
				match(T__3);
				setState(84);
				((SingleVarContext)_localctx).exp = statement();
				}
				break;
			case 2:
				_localctx = new MultiVarContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(87);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
				case 1:
					{
					setState(85);
					match(T__2);
					}
					break;
				case 2:
					{
					}
					break;
				}
				setState(89);
				((MultiVarContext)_localctx).name = varname_list(0);
				setState(90);
				match(T__3);
				setState(91);
				((MultiVarContext)_localctx).vals = varname_list(0);
				}
				break;
			case 3:
				_localctx = new ListVarContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(95);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__2:
					{
					setState(93);
					match(T__2);
					}
					break;
				case VARNAME:
					{
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(97);
				((ListVarContext)_localctx).name = match(VARNAME);
				setState(98);
				match(T__3);
				setState(99);
				match(T__4);
				setState(100);
				((ListVarContext)_localctx).vals = var_list(0);
				setState(101);
				match(T__5);
				}
				break;
			case 4:
				_localctx = new ListSetContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(105);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__2:
					{
					setState(103);
					match(T__2);
					}
					break;
				case VARNAME:
					{
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(107);
				((ListSetContext)_localctx).name = match(VARNAME);
				setState(108);
				match(T__4);
				setState(109);
				((ListSetContext)_localctx).index = match(NUM);
				setState(110);
				match(T__5);
				setState(111);
				match(T__3);
				setState(112);
				((ListSetContext)_localctx).exp = statement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarContext extends ParserRuleContext {
		public VarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var; }
	 
		public VarContext() { }
		public void copyFrom(VarContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ListGetContext extends VarContext {
		public Token name;
		public Token index;
		public TerminalNode VARNAME() { return getToken(GrammarParser.VARNAME, 0); }
		public TerminalNode NUM() { return getToken(GrammarParser.NUM, 0); }
		public ListGetContext(VarContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VarNameContext extends VarContext {
		public Token name;
		public TerminalNode VARNAME() { return getToken(GrammarParser.VARNAME, 0); }
		public VarNameContext(VarContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class InvertVarContext extends VarContext {
		public Token inv;
		public Token name;
		public TerminalNode VARNAME() { return getToken(GrammarParser.VARNAME, 0); }
		public InvertVarContext(VarContext ctx) { copyFrom(ctx); }
	}

	public final VarContext var() throws RecognitionException {
		VarContext _localctx = new VarContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_var);
		try {
			setState(122);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				_localctx = new InvertVarContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(115);
				((InvertVarContext)_localctx).inv = match(T__6);
				setState(116);
				((InvertVarContext)_localctx).name = match(VARNAME);
				}
				break;
			case 2:
				_localctx = new VarNameContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(117);
				((VarNameContext)_localctx).name = match(VARNAME);
				}
				break;
			case 3:
				_localctx = new ListGetContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(118);
				((ListGetContext)_localctx).name = match(VARNAME);
				setState(119);
				match(T__4);
				setState(120);
				((ListGetContext)_localctx).index = match(NUM);
				setState(121);
				match(T__5);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_loopContext extends ParserRuleContext {
		public Token value;
		public StatementContext array;
		public BracketsContext stmts;
		public TerminalNode VARNAME() { return getToken(GrammarParser.VARNAME, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public BracketsContext brackets() {
			return getRuleContext(BracketsContext.class,0);
		}
		public For_loopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_loop; }
	}

	public final For_loopContext for_loop() throws RecognitionException {
		For_loopContext _localctx = new For_loopContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_for_loop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			match(T__7);
			setState(125);
			match(T__8);
			setState(126);
			((For_loopContext)_localctx).value = match(VARNAME);
			setState(127);
			match(T__9);
			setState(128);
			((For_loopContext)_localctx).array = statement();
			setState(129);
			match(T__10);
			setState(130);
			match(T__11);
			setState(131);
			((For_loopContext)_localctx).stmts = brackets(0);
			setState(132);
			match(T__12);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Conditional_statementContext extends ParserRuleContext {
		public Token label;
		public TruthContext t;
		public BracketsContext stmts;
		public ElifContext elseif;
		public TruthContext truth() {
			return getRuleContext(TruthContext.class,0);
		}
		public BracketsContext brackets() {
			return getRuleContext(BracketsContext.class,0);
		}
		public ElifContext elif() {
			return getRuleContext(ElifContext.class,0);
		}
		public Conditional_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditional_statement; }
	}

	public final Conditional_statementContext conditional_statement() throws RecognitionException {
		Conditional_statementContext _localctx = new Conditional_statementContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_conditional_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			((Conditional_statementContext)_localctx).label = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==T__13 || _la==T__14) ) {
				((Conditional_statementContext)_localctx).label = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(135);
			match(T__8);
			setState(136);
			((Conditional_statementContext)_localctx).t = truth(0);
			setState(137);
			match(T__10);
			setState(138);
			match(T__11);
			setState(139);
			((Conditional_statementContext)_localctx).stmts = brackets(0);
			setState(140);
			match(T__12);
			setState(142);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(141);
				((Conditional_statementContext)_localctx).elseif = elif(0);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ElifContext extends ParserRuleContext {
		public ElifContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elif; }
	 
		public ElifContext() { }
		public void copyFrom(ElifContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ElseIfContext extends ElifContext {
		public ElifContext lhs;
		public ElifContext rhs;
		public List<ElifContext> elif() {
			return getRuleContexts(ElifContext.class);
		}
		public ElifContext elif(int i) {
			return getRuleContext(ElifContext.class,i);
		}
		public ElseIfContext(ElifContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ElseElifContext extends ElifContext {
		public ElseContext else_() {
			return getRuleContext(ElseContext.class,0);
		}
		public ElseElifContext(ElifContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AtomElifContext extends ElifContext {
		public TruthContext t;
		public BracketsContext stmts;
		public TruthContext truth() {
			return getRuleContext(TruthContext.class,0);
		}
		public BracketsContext brackets() {
			return getRuleContext(BracketsContext.class,0);
		}
		public AtomElifContext(ElifContext ctx) { copyFrom(ctx); }
	}

	public final ElifContext elif() throws RecognitionException {
		return elif(0);
	}

	private ElifContext elif(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ElifContext _localctx = new ElifContext(_ctx, _parentState);
		ElifContext _prevctx = _localctx;
		int _startState = 16;
		enterRecursionRule(_localctx, 16, RULE_elif, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(154);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__15:
				{
				_localctx = new AtomElifContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(145);
				match(T__15);
				setState(146);
				match(T__8);
				setState(147);
				((AtomElifContext)_localctx).t = truth(0);
				setState(148);
				match(T__10);
				setState(149);
				match(T__11);
				setState(150);
				((AtomElifContext)_localctx).stmts = brackets(0);
				setState(151);
				match(T__12);
				}
				break;
			case T__16:
				{
				_localctx = new ElseElifContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(153);
				else_();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(160);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ElseIfContext(new ElifContext(_parentctx, _parentState));
					((ElseIfContext)_localctx).lhs = _prevctx;
					pushNewRecursionContext(_localctx, _startState, RULE_elif);
					setState(156);
					if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
					setState(157);
					((ElseIfContext)_localctx).rhs = elif(4);
					}
					} 
				}
				setState(162);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ElseContext extends ParserRuleContext {
		public BracketsContext stmts;
		public BracketsContext brackets() {
			return getRuleContext(BracketsContext.class,0);
		}
		public ElseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_else; }
	}

	public final ElseContext else_() throws RecognitionException {
		ElseContext _localctx = new ElseContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_else);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(163);
			match(T__16);
			setState(164);
			match(T__11);
			setState(165);
			((ElseContext)_localctx).stmts = brackets(0);
			setState(166);
			match(T__12);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TruthContext extends ParserRuleContext {
		public TruthContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_truth; }
	 
		public TruthContext() { }
		public void copyFrom(TruthContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParenTruthContext extends TruthContext {
		public TruthContext t;
		public TruthContext truth() {
			return getRuleContext(TruthContext.class,0);
		}
		public ParenTruthContext(TruthContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AtomTruthContext extends TruthContext {
		public StatementContext atom;
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public AtomTruthContext(TruthContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LogicTruthContext extends TruthContext {
		public TruthContext lhs;
		public Token logic;
		public TruthContext rhs;
		public List<TruthContext> truth() {
			return getRuleContexts(TruthContext.class);
		}
		public TruthContext truth(int i) {
			return getRuleContext(TruthContext.class,i);
		}
		public LogicTruthContext(TruthContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DualTruthContext extends TruthContext {
		public StatementContext lhs;
		public Token operand;
		public StatementContext rhs;
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public DualTruthContext(TruthContext ctx) { copyFrom(ctx); }
	}

	public final TruthContext truth() throws RecognitionException {
		return truth(0);
	}

	private TruthContext truth(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		TruthContext _localctx = new TruthContext(_ctx, _parentState);
		TruthContext _prevctx = _localctx;
		int _startState = 20;
		enterRecursionRule(_localctx, 20, RULE_truth, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(178);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				{
				_localctx = new ParenTruthContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(169);
				match(T__8);
				setState(170);
				((ParenTruthContext)_localctx).t = truth(0);
				setState(171);
				match(T__10);
				}
				break;
			case 2:
				{
				_localctx = new DualTruthContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(173);
				((DualTruthContext)_localctx).lhs = statement();
				setState(174);
				((DualTruthContext)_localctx).operand = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 66060288L) != 0)) ) {
					((DualTruthContext)_localctx).operand = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(175);
				((DualTruthContext)_localctx).rhs = statement();
				}
				break;
			case 3:
				{
				_localctx = new AtomTruthContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(177);
				((AtomTruthContext)_localctx).atom = statement();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(185);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new LogicTruthContext(new TruthContext(_parentctx, _parentState));
					((LogicTruthContext)_localctx).lhs = _prevctx;
					pushNewRecursionContext(_localctx, _startState, RULE_truth);
					setState(180);
					if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
					setState(181);
					((LogicTruthContext)_localctx).logic = _input.LT(1);
					_la = _input.LA(1);
					if ( !(_la==T__17 || _la==T__18) ) {
						((LogicTruthContext)_localctx).logic = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(182);
					((LogicTruthContext)_localctx).rhs = truth(4);
					}
					} 
				}
				setState(187);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Function_defContext extends ParserRuleContext {
		public Token name;
		public Varname_listContext args;
		public BracketsContext stmts;
		public TerminalNode VARNAME() { return getToken(GrammarParser.VARNAME, 0); }
		public Varname_listContext varname_list() {
			return getRuleContext(Varname_listContext.class,0);
		}
		public BracketsContext brackets() {
			return getRuleContext(BracketsContext.class,0);
		}
		public Function_defContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_def; }
	}

	public final Function_defContext function_def() throws RecognitionException {
		Function_defContext _localctx = new Function_defContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_function_def);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__2:
				{
				setState(188);
				match(T__2);
				}
				break;
			case T__25:
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(192);
			match(T__25);
			setState(193);
			((Function_defContext)_localctx).name = match(VARNAME);
			setState(194);
			match(T__8);
			setState(195);
			((Function_defContext)_localctx).args = varname_list(0);
			setState(196);
			match(T__10);
			setState(197);
			match(T__11);
			setState(198);
			((Function_defContext)_localctx).stmts = brackets(0);
			setState(199);
			match(T__12);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Varname_listContext extends ParserRuleContext {
		public Varname_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varname_list; }
	 
		public Varname_listContext() { }
		public void copyFrom(Varname_listContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NullVarnameContext extends Varname_listContext {
		public NullVarnameContext(Varname_listContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AtomVarnameContext extends Varname_listContext {
		public Token atom;
		public TerminalNode VARNAME() { return getToken(GrammarParser.VARNAME, 0); }
		public AtomVarnameContext(Varname_listContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CommaVarnameContext extends Varname_listContext {
		public Varname_listContext lhs;
		public Varname_listContext rhs;
		public List<Varname_listContext> varname_list() {
			return getRuleContexts(Varname_listContext.class);
		}
		public Varname_listContext varname_list(int i) {
			return getRuleContext(Varname_listContext.class,i);
		}
		public CommaVarnameContext(Varname_listContext ctx) { copyFrom(ctx); }
	}

	public final Varname_listContext varname_list() throws RecognitionException {
		return varname_list(0);
	}

	private Varname_listContext varname_list(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Varname_listContext _localctx = new Varname_listContext(_ctx, _parentState);
		Varname_listContext _prevctx = _localctx;
		int _startState = 24;
		enterRecursionRule(_localctx, 24, RULE_varname_list, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				{
				_localctx = new AtomVarnameContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(202);
				((AtomVarnameContext)_localctx).atom = match(VARNAME);
				}
				break;
			case 2:
				{
				_localctx = new NullVarnameContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(211);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new CommaVarnameContext(new Varname_listContext(_parentctx, _parentState));
					((CommaVarnameContext)_localctx).lhs = _prevctx;
					pushNewRecursionContext(_localctx, _startState, RULE_varname_list);
					setState(206);
					if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
					setState(207);
					match(T__26);
					setState(208);
					((CommaVarnameContext)_localctx).rhs = varname_list(4);
					}
					} 
				}
				setState(213);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Var_listContext extends ParserRuleContext {
		public Var_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_list; }
	 
		public Var_listContext() { }
		public void copyFrom(Var_listContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NullVarlistContext extends Var_listContext {
		public NullVarlistContext(Var_listContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AtomVarlistContext extends Var_listContext {
		public StatementContext atom;
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public AtomVarlistContext(Var_listContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CommaVarlistContext extends Var_listContext {
		public Var_listContext lhs;
		public Var_listContext rhs;
		public List<Var_listContext> var_list() {
			return getRuleContexts(Var_listContext.class);
		}
		public Var_listContext var_list(int i) {
			return getRuleContext(Var_listContext.class,i);
		}
		public CommaVarlistContext(Var_listContext ctx) { copyFrom(ctx); }
	}

	public final Var_listContext var_list() throws RecognitionException {
		return var_list(0);
	}

	private Var_listContext var_list(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Var_listContext _localctx = new Var_listContext(_ctx, _parentState);
		Var_listContext _prevctx = _localctx;
		int _startState = 26;
		enterRecursionRule(_localctx, 26, RULE_var_list, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(217);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				{
				_localctx = new AtomVarlistContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(215);
				((AtomVarlistContext)_localctx).atom = statement();
				}
				break;
			case 2:
				{
				_localctx = new NullVarlistContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(224);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new CommaVarlistContext(new Var_listContext(_parentctx, _parentState));
					((CommaVarlistContext)_localctx).lhs = _prevctx;
					pushNewRecursionContext(_localctx, _startState, RULE_var_list);
					setState(219);
					if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
					setState(220);
					match(T__26);
					setState(221);
					((CommaVarlistContext)_localctx).rhs = var_list(4);
					}
					} 
				}
				setState(226);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BracketsContext extends ParserRuleContext {
		public BracketsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_brackets; }
	 
		public BracketsContext() { }
		public void copyFrom(BracketsContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AtomBracketStatementContext extends BracketsContext {
		public Bracket_statementContext atom;
		public Bracket_statementContext bracket_statement() {
			return getRuleContext(Bracket_statementContext.class,0);
		}
		public AtomBracketStatementContext(BracketsContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SemiBracketsContext extends BracketsContext {
		public BracketsContext lhs;
		public BracketsContext rhs;
		public List<BracketsContext> brackets() {
			return getRuleContexts(BracketsContext.class);
		}
		public BracketsContext brackets(int i) {
			return getRuleContext(BracketsContext.class,i);
		}
		public SemiBracketsContext(BracketsContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AtomBracketsContext extends BracketsContext {
		public StatementContext atom;
		public TerminalNode SEMI() { return getToken(GrammarParser.SEMI, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public AtomBracketsContext(BracketsContext ctx) { copyFrom(ctx); }
	}

	public final BracketsContext brackets() throws RecognitionException {
		return brackets(0);
	}

	private BracketsContext brackets(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		BracketsContext _localctx = new BracketsContext(_ctx, _parentState);
		BracketsContext _prevctx = _localctx;
		int _startState = 28;
		enterRecursionRule(_localctx, 28, RULE_brackets, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				{
				_localctx = new AtomBracketsContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(228);
				((AtomBracketsContext)_localctx).atom = statement();
				setState(229);
				match(SEMI);
				}
				break;
			case 2:
				{
				_localctx = new AtomBracketStatementContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(231);
				((AtomBracketStatementContext)_localctx).atom = bracket_statement();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(238);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new SemiBracketsContext(new BracketsContext(_parentctx, _parentState));
					((SemiBracketsContext)_localctx).lhs = _prevctx;
					pushNewRecursionContext(_localctx, _startState, RULE_brackets);
					setState(234);
					if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
					setState(235);
					((SemiBracketsContext)_localctx).rhs = brackets(4);
					}
					} 
				}
				setState(240);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StrExprContext extends ExprContext {
		public Token atom;
		public TerminalNode StringLiteral() { return getToken(GrammarParser.StringLiteral, 0); }
		public StrExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FloatExprContext extends ExprContext {
		public Token atom;
		public TerminalNode FLOAT() { return getToken(GrammarParser.FLOAT, 0); }
		public FloatExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VarExprContext extends ExprContext {
		public VarContext atom;
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public VarExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IntExprContext extends ExprContext {
		public Token atom;
		public TerminalNode NUM() { return getToken(GrammarParser.NUM, 0); }
		public IntExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OpExprContext extends ExprContext {
		public ExprContext lhs;
		public Token op;
		public ExprContext rhs;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MUL() { return getToken(GrammarParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(GrammarParser.DIV, 0); }
		public TerminalNode ADD() { return getToken(GrammarParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(GrammarParser.SUB, 0); }
		public TerminalNode MOD() { return getToken(GrammarParser.MOD, 0); }
		public OpExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NullExprContext extends ExprContext {
		public Token atom;
		public TerminalNode NULL() { return getToken(GrammarParser.NULL, 0); }
		public NullExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Function_callContext extends ExprContext {
		public Token name;
		public Var_listContext args;
		public TerminalNode VARNAME() { return getToken(GrammarParser.VARNAME, 0); }
		public Var_listContext var_list() {
			return getRuleContext(Var_listContext.class,0);
		}
		public Function_callContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NegExprContext extends ExprContext {
		public ExprContext exp;
		public TerminalNode SUB() { return getToken(GrammarParser.SUB, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public NegExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParensExprContext extends ExprContext {
		public ExprContext exp;
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ParensExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BoolExprContext extends ExprContext {
		public Token atom;
		public TerminalNode BOOL() { return getToken(GrammarParser.BOOL, 0); }
		public BoolExprContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 30;
		enterRecursionRule(_localctx, 30, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(259);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				{
				_localctx = new ParensExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(242);
				match(T__8);
				setState(243);
				((ParensExprContext)_localctx).exp = expr(0);
				setState(244);
				match(T__10);
				}
				break;
			case 2:
				{
				_localctx = new NegExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(246);
				match(SUB);
				setState(247);
				((NegExprContext)_localctx).exp = expr(10);
				}
				break;
			case 3:
				{
				_localctx = new IntExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(248);
				((IntExprContext)_localctx).atom = match(NUM);
				}
				break;
			case 4:
				{
				_localctx = new BoolExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(249);
				((BoolExprContext)_localctx).atom = match(BOOL);
				}
				break;
			case 5:
				{
				_localctx = new StrExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(250);
				((StrExprContext)_localctx).atom = match(StringLiteral);
				}
				break;
			case 6:
				{
				_localctx = new NullExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(251);
				((NullExprContext)_localctx).atom = match(NULL);
				}
				break;
			case 7:
				{
				_localctx = new FloatExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(252);
				((FloatExprContext)_localctx).atom = match(FLOAT);
				}
				break;
			case 8:
				{
				_localctx = new VarExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(253);
				((VarExprContext)_localctx).atom = var();
				}
				break;
			case 9:
				{
				_localctx = new Function_callContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(254);
				((Function_callContext)_localctx).name = match(VARNAME);
				setState(255);
				match(T__8);
				setState(256);
				((Function_callContext)_localctx).args = var_list(0);
				setState(257);
				match(T__10);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(269);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,29,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(267);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
					case 1:
						{
						_localctx = new OpExprContext(new ExprContext(_parentctx, _parentState));
						((OpExprContext)_localctx).lhs = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(261);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(262);
						((OpExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
							((OpExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(263);
						((OpExprContext)_localctx).rhs = expr(10);
						}
						break;
					case 2:
						{
						_localctx = new OpExprContext(new ExprContext(_parentctx, _parentState));
						((OpExprContext)_localctx).lhs = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(264);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(265);
						((OpExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 10445360463872L) != 0)) ) {
							((OpExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(266);
						((OpExprContext)_localctx).rhs = expr(9);
						}
						break;
					}
					} 
				}
				setState(271);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,29,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 8:
			return elif_sempred((ElifContext)_localctx, predIndex);
		case 10:
			return truth_sempred((TruthContext)_localctx, predIndex);
		case 12:
			return varname_list_sempred((Varname_listContext)_localctx, predIndex);
		case 13:
			return var_list_sempred((Var_listContext)_localctx, predIndex);
		case 14:
			return brackets_sempred((BracketsContext)_localctx, predIndex);
		case 15:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean elif_sempred(ElifContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 3);
		}
		return true;
	}
	private boolean truth_sempred(TruthContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 3);
		}
		return true;
	}
	private boolean varname_list_sempred(Varname_listContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 3);
		}
		return true;
	}
	private boolean var_list_sempred(Var_listContext _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 3);
		}
		return true;
	}
	private boolean brackets_sempred(BracketsContext _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 3);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 5:
			return precpred(_ctx, 9);
		case 6:
			return precpred(_ctx, 8);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001+\u0111\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0001\u0000\u0001\u0000\u0003\u0000#\b\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0005\u0000(\b\u0000\n\u0000\f\u0000+\t\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0003\u00010\b\u0001\u0001\u0001\u0001\u0001"+
		"\u0005\u00014\b\u0001\n\u0001\f\u00017\t\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u0001<\b\u0001\u0003\u0001>\b\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0003\u0002C\b\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0005\u0003H\b\u0003\n\u0003\f\u0003K\t\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0003\u0004Q\b\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004X\b\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003"+
		"\u0004`\b\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004j\b\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003"+
		"\u0004r\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0003\u0005{\b\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007\u008f"+
		"\b\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0003\b\u009b\b\b\u0001\b\u0001\b\u0005\b\u009f\b\b"+
		"\n\b\f\b\u00a2\t\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003"+
		"\n\u00b3\b\n\u0001\n\u0001\n\u0001\n\u0005\n\u00b8\b\n\n\n\f\n\u00bb\t"+
		"\n\u0001\u000b\u0001\u000b\u0003\u000b\u00bf\b\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0003\f\u00cd\b\f\u0001\f\u0001"+
		"\f\u0001\f\u0005\f\u00d2\b\f\n\f\f\f\u00d5\t\f\u0001\r\u0001\r\u0001\r"+
		"\u0003\r\u00da\b\r\u0001\r\u0001\r\u0001\r\u0005\r\u00df\b\r\n\r\f\r\u00e2"+
		"\t\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003"+
		"\u000e\u00e9\b\u000e\u0001\u000e\u0001\u000e\u0005\u000e\u00ed\b\u000e"+
		"\n\u000e\f\u000e\u00f0\t\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u0104\b\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u010c"+
		"\b\u000f\n\u000f\f\u000f\u010f\t\u000f\u0001\u000f\u0000\u0006\u0010\u0014"+
		"\u0018\u001a\u001c\u001e\u0010\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010"+
		"\u0012\u0014\u0016\u0018\u001a\u001c\u001e\u0000\u0005\u0001\u0000\u000e"+
		"\u000f\u0001\u0000\u0014\u0019\u0001\u0000\u0012\u0013\u0001\u0000)*\u0002"+
		"\u0000\'(++\u012c\u0000)\u0001\u0000\u0000\u0000\u0002=\u0001\u0000\u0000"+
		"\u0000\u0004B\u0001\u0000\u0000\u0000\u0006D\u0001\u0000\u0000\u0000\b"+
		"q\u0001\u0000\u0000\u0000\nz\u0001\u0000\u0000\u0000\f|\u0001\u0000\u0000"+
		"\u0000\u000e\u0086\u0001\u0000\u0000\u0000\u0010\u009a\u0001\u0000\u0000"+
		"\u0000\u0012\u00a3\u0001\u0000\u0000\u0000\u0014\u00b2\u0001\u0000\u0000"+
		"\u0000\u0016\u00be\u0001\u0000\u0000\u0000\u0018\u00cc\u0001\u0000\u0000"+
		"\u0000\u001a\u00d9\u0001\u0000\u0000\u0000\u001c\u00e8\u0001\u0000\u0000"+
		"\u0000\u001e\u0103\u0001\u0000\u0000\u0000 #\u0003\u0002\u0001\u0000!"+
		"#\u0003\u0006\u0003\u0000\" \u0001\u0000\u0000\u0000\"!\u0001\u0000\u0000"+
		"\u0000#$\u0001\u0000\u0000\u0000$%\u0005\u001c\u0000\u0000%(\u0001\u0000"+
		"\u0000\u0000&(\u0003\u0004\u0002\u0000\'\"\u0001\u0000\u0000\u0000\'&"+
		"\u0001\u0000\u0000\u0000(+\u0001\u0000\u0000\u0000)\'\u0001\u0000\u0000"+
		"\u0000)*\u0001\u0000\u0000\u0000*\u0001\u0001\u0000\u0000\u0000+)\u0001"+
		"\u0000\u0000\u0000,0\u0003\u001e\u000f\u0000-0\u0003\b\u0004\u0000.0\u0003"+
		"\n\u0005\u0000/,\u0001\u0000\u0000\u0000/-\u0001\u0000\u0000\u0000/.\u0001"+
		"\u0000\u0000\u00000>\u0001\u0000\u0000\u000012\u0005&\u0000\u000024\u0005"+
		"\u0001\u0000\u000031\u0001\u0000\u0000\u000047\u0001\u0000\u0000\u0000"+
		"53\u0001\u0000\u0000\u000056\u0001\u0000\u0000\u00006;\u0001\u0000\u0000"+
		"\u000075\u0001\u0000\u0000\u00008<\u0003\u001e\u000f\u00009<\u0003\b\u0004"+
		"\u0000:<\u0003\n\u0005\u0000;8\u0001\u0000\u0000\u0000;9\u0001\u0000\u0000"+
		"\u0000;:\u0001\u0000\u0000\u0000<>\u0001\u0000\u0000\u0000=/\u0001\u0000"+
		"\u0000\u0000=5\u0001\u0000\u0000\u0000>\u0003\u0001\u0000\u0000\u0000"+
		"?C\u0003\u000e\u0007\u0000@C\u0003\u0016\u000b\u0000AC\u0003\f\u0006\u0000"+
		"B?\u0001\u0000\u0000\u0000B@\u0001\u0000\u0000\u0000BA\u0001\u0000\u0000"+
		"\u0000C\u0005\u0001\u0000\u0000\u0000DI\u0005\u0002\u0000\u0000EF\u0005"+
		"&\u0000\u0000FH\t\u0000\u0000\u0000GE\u0001\u0000\u0000\u0000HK\u0001"+
		"\u0000\u0000\u0000IG\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000"+
		"JL\u0001\u0000\u0000\u0000KI\u0001\u0000\u0000\u0000LM\u0005&\u0000\u0000"+
		"M\u0007\u0001\u0000\u0000\u0000NQ\u0005\u0003\u0000\u0000OQ\u0001\u0000"+
		"\u0000\u0000PN\u0001\u0000\u0000\u0000PO\u0001\u0000\u0000\u0000QR\u0001"+
		"\u0000\u0000\u0000RS\u0005&\u0000\u0000ST\u0005\u0004\u0000\u0000Tr\u0003"+
		"\u0002\u0001\u0000UX\u0005\u0003\u0000\u0000VX\u0001\u0000\u0000\u0000"+
		"WU\u0001\u0000\u0000\u0000WV\u0001\u0000\u0000\u0000XY\u0001\u0000\u0000"+
		"\u0000YZ\u0003\u0018\f\u0000Z[\u0005\u0004\u0000\u0000[\\\u0003\u0018"+
		"\f\u0000\\r\u0001\u0000\u0000\u0000]`\u0005\u0003\u0000\u0000^`\u0001"+
		"\u0000\u0000\u0000_]\u0001\u0000\u0000\u0000_^\u0001\u0000\u0000\u0000"+
		"`a\u0001\u0000\u0000\u0000ab\u0005&\u0000\u0000bc\u0005\u0004\u0000\u0000"+
		"cd\u0005\u0005\u0000\u0000de\u0003\u001a\r\u0000ef\u0005\u0006\u0000\u0000"+
		"fr\u0001\u0000\u0000\u0000gj\u0005\u0003\u0000\u0000hj\u0001\u0000\u0000"+
		"\u0000ig\u0001\u0000\u0000\u0000ih\u0001\u0000\u0000\u0000jk\u0001\u0000"+
		"\u0000\u0000kl\u0005&\u0000\u0000lm\u0005\u0005\u0000\u0000mn\u0005\u001e"+
		"\u0000\u0000no\u0005\u0006\u0000\u0000op\u0005\u0004\u0000\u0000pr\u0003"+
		"\u0002\u0001\u0000qP\u0001\u0000\u0000\u0000qW\u0001\u0000\u0000\u0000"+
		"q_\u0001\u0000\u0000\u0000qi\u0001\u0000\u0000\u0000r\t\u0001\u0000\u0000"+
		"\u0000st\u0005\u0007\u0000\u0000t{\u0005&\u0000\u0000u{\u0005&\u0000\u0000"+
		"vw\u0005&\u0000\u0000wx\u0005\u0005\u0000\u0000xy\u0005\u001e\u0000\u0000"+
		"y{\u0005\u0006\u0000\u0000zs\u0001\u0000\u0000\u0000zu\u0001\u0000\u0000"+
		"\u0000zv\u0001\u0000\u0000\u0000{\u000b\u0001\u0000\u0000\u0000|}\u0005"+
		"\b\u0000\u0000}~\u0005\t\u0000\u0000~\u007f\u0005&\u0000\u0000\u007f\u0080"+
		"\u0005\n\u0000\u0000\u0080\u0081\u0003\u0002\u0001\u0000\u0081\u0082\u0005"+
		"\u000b\u0000\u0000\u0082\u0083\u0005\f\u0000\u0000\u0083\u0084\u0003\u001c"+
		"\u000e\u0000\u0084\u0085\u0005\r\u0000\u0000\u0085\r\u0001\u0000\u0000"+
		"\u0000\u0086\u0087\u0007\u0000\u0000\u0000\u0087\u0088\u0005\t\u0000\u0000"+
		"\u0088\u0089\u0003\u0014\n\u0000\u0089\u008a\u0005\u000b\u0000\u0000\u008a"+
		"\u008b\u0005\f\u0000\u0000\u008b\u008c\u0003\u001c\u000e\u0000\u008c\u008e"+
		"\u0005\r\u0000\u0000\u008d\u008f\u0003\u0010\b\u0000\u008e\u008d\u0001"+
		"\u0000\u0000\u0000\u008e\u008f\u0001\u0000\u0000\u0000\u008f\u000f\u0001"+
		"\u0000\u0000\u0000\u0090\u0091\u0006\b\uffff\uffff\u0000\u0091\u0092\u0005"+
		"\u0010\u0000\u0000\u0092\u0093\u0005\t\u0000\u0000\u0093\u0094\u0003\u0014"+
		"\n\u0000\u0094\u0095\u0005\u000b\u0000\u0000\u0095\u0096\u0005\f\u0000"+
		"\u0000\u0096\u0097\u0003\u001c\u000e\u0000\u0097\u0098\u0005\r\u0000\u0000"+
		"\u0098\u009b\u0001\u0000\u0000\u0000\u0099\u009b\u0003\u0012\t\u0000\u009a"+
		"\u0090\u0001\u0000\u0000\u0000\u009a\u0099\u0001\u0000\u0000\u0000\u009b"+
		"\u00a0\u0001\u0000\u0000\u0000\u009c\u009d\n\u0003\u0000\u0000\u009d\u009f"+
		"\u0003\u0010\b\u0004\u009e\u009c\u0001\u0000\u0000\u0000\u009f\u00a2\u0001"+
		"\u0000\u0000\u0000\u00a0\u009e\u0001\u0000\u0000\u0000\u00a0\u00a1\u0001"+
		"\u0000\u0000\u0000\u00a1\u0011\u0001\u0000\u0000\u0000\u00a2\u00a0\u0001"+
		"\u0000\u0000\u0000\u00a3\u00a4\u0005\u0011\u0000\u0000\u00a4\u00a5\u0005"+
		"\f\u0000\u0000\u00a5\u00a6\u0003\u001c\u000e\u0000\u00a6\u00a7\u0005\r"+
		"\u0000\u0000\u00a7\u0013\u0001\u0000\u0000\u0000\u00a8\u00a9\u0006\n\uffff"+
		"\uffff\u0000\u00a9\u00aa\u0005\t\u0000\u0000\u00aa\u00ab\u0003\u0014\n"+
		"\u0000\u00ab\u00ac\u0005\u000b\u0000\u0000\u00ac\u00b3\u0001\u0000\u0000"+
		"\u0000\u00ad\u00ae\u0003\u0002\u0001\u0000\u00ae\u00af\u0007\u0001\u0000"+
		"\u0000\u00af\u00b0\u0003\u0002\u0001\u0000\u00b0\u00b3\u0001\u0000\u0000"+
		"\u0000\u00b1\u00b3\u0003\u0002\u0001\u0000\u00b2\u00a8\u0001\u0000\u0000"+
		"\u0000\u00b2\u00ad\u0001\u0000\u0000\u0000\u00b2\u00b1\u0001\u0000\u0000"+
		"\u0000\u00b3\u00b9\u0001\u0000\u0000\u0000\u00b4\u00b5\n\u0003\u0000\u0000"+
		"\u00b5\u00b6\u0007\u0002\u0000\u0000\u00b6\u00b8\u0003\u0014\n\u0004\u00b7"+
		"\u00b4\u0001\u0000\u0000\u0000\u00b8\u00bb\u0001\u0000\u0000\u0000\u00b9"+
		"\u00b7\u0001\u0000\u0000\u0000\u00b9\u00ba\u0001\u0000\u0000\u0000\u00ba"+
		"\u0015\u0001\u0000\u0000\u0000\u00bb\u00b9\u0001\u0000\u0000\u0000\u00bc"+
		"\u00bf\u0005\u0003\u0000\u0000\u00bd\u00bf\u0001\u0000\u0000\u0000\u00be"+
		"\u00bc\u0001\u0000\u0000\u0000\u00be\u00bd\u0001\u0000\u0000\u0000\u00bf"+
		"\u00c0\u0001\u0000\u0000\u0000\u00c0\u00c1\u0005\u001a\u0000\u0000\u00c1"+
		"\u00c2\u0005&\u0000\u0000\u00c2\u00c3\u0005\t\u0000\u0000\u00c3\u00c4"+
		"\u0003\u0018\f\u0000\u00c4\u00c5\u0005\u000b\u0000\u0000\u00c5\u00c6\u0005"+
		"\f\u0000\u0000\u00c6\u00c7\u0003\u001c\u000e\u0000\u00c7\u00c8\u0005\r"+
		"\u0000\u0000\u00c8\u0017\u0001\u0000\u0000\u0000\u00c9\u00ca\u0006\f\uffff"+
		"\uffff\u0000\u00ca\u00cd\u0005&\u0000\u0000\u00cb\u00cd\u0001\u0000\u0000"+
		"\u0000\u00cc\u00c9\u0001\u0000\u0000\u0000\u00cc\u00cb\u0001\u0000\u0000"+
		"\u0000\u00cd\u00d3\u0001\u0000\u0000\u0000\u00ce\u00cf\n\u0003\u0000\u0000"+
		"\u00cf\u00d0\u0005\u001b\u0000\u0000\u00d0\u00d2\u0003\u0018\f\u0004\u00d1"+
		"\u00ce\u0001\u0000\u0000\u0000\u00d2\u00d5\u0001\u0000\u0000\u0000\u00d3"+
		"\u00d1\u0001\u0000\u0000\u0000\u00d3\u00d4\u0001\u0000\u0000\u0000\u00d4"+
		"\u0019\u0001\u0000\u0000\u0000\u00d5\u00d3\u0001\u0000\u0000\u0000\u00d6"+
		"\u00d7\u0006\r\uffff\uffff\u0000\u00d7\u00da\u0003\u0002\u0001\u0000\u00d8"+
		"\u00da\u0001\u0000\u0000\u0000\u00d9\u00d6\u0001\u0000\u0000\u0000\u00d9"+
		"\u00d8\u0001\u0000\u0000\u0000\u00da\u00e0\u0001\u0000\u0000\u0000\u00db"+
		"\u00dc\n\u0003\u0000\u0000\u00dc\u00dd\u0005\u001b\u0000\u0000\u00dd\u00df"+
		"\u0003\u001a\r\u0004\u00de\u00db\u0001\u0000\u0000\u0000\u00df\u00e2\u0001"+
		"\u0000\u0000\u0000\u00e0\u00de\u0001\u0000\u0000\u0000\u00e0\u00e1\u0001"+
		"\u0000\u0000\u0000\u00e1\u001b\u0001\u0000\u0000\u0000\u00e2\u00e0\u0001"+
		"\u0000\u0000\u0000\u00e3\u00e4\u0006\u000e\uffff\uffff\u0000\u00e4\u00e5"+
		"\u0003\u0002\u0001\u0000\u00e5\u00e6\u0005\u001c\u0000\u0000\u00e6\u00e9"+
		"\u0001\u0000\u0000\u0000\u00e7\u00e9\u0003\u0004\u0002\u0000\u00e8\u00e3"+
		"\u0001\u0000\u0000\u0000\u00e8\u00e7\u0001\u0000\u0000\u0000\u00e9\u00ee"+
		"\u0001\u0000\u0000\u0000\u00ea\u00eb\n\u0003\u0000\u0000\u00eb\u00ed\u0003"+
		"\u001c\u000e\u0004\u00ec\u00ea\u0001\u0000\u0000\u0000\u00ed\u00f0\u0001"+
		"\u0000\u0000\u0000\u00ee\u00ec\u0001\u0000\u0000\u0000\u00ee\u00ef\u0001"+
		"\u0000\u0000\u0000\u00ef\u001d\u0001\u0000\u0000\u0000\u00f0\u00ee\u0001"+
		"\u0000\u0000\u0000\u00f1\u00f2\u0006\u000f\uffff\uffff\u0000\u00f2\u00f3"+
		"\u0005\t\u0000\u0000\u00f3\u00f4\u0003\u001e\u000f\u0000\u00f4\u00f5\u0005"+
		"\u000b\u0000\u0000\u00f5\u0104\u0001\u0000\u0000\u0000\u00f6\u00f7\u0005"+
		"(\u0000\u0000\u00f7\u0104\u0003\u001e\u000f\n\u00f8\u0104\u0005\u001e"+
		"\u0000\u0000\u00f9\u0104\u0005 \u0000\u0000\u00fa\u0104\u0005!\u0000\u0000"+
		"\u00fb\u0104\u0005#\u0000\u0000\u00fc\u0104\u0005\u001f\u0000\u0000\u00fd"+
		"\u0104\u0003\n\u0005\u0000\u00fe\u00ff\u0005&\u0000\u0000\u00ff\u0100"+
		"\u0005\t\u0000\u0000\u0100\u0101\u0003\u001a\r\u0000\u0101\u0102\u0005"+
		"\u000b\u0000\u0000\u0102\u0104\u0001\u0000\u0000\u0000\u0103\u00f1\u0001"+
		"\u0000\u0000\u0000\u0103\u00f6\u0001\u0000\u0000\u0000\u0103\u00f8\u0001"+
		"\u0000\u0000\u0000\u0103\u00f9\u0001\u0000\u0000\u0000\u0103\u00fa\u0001"+
		"\u0000\u0000\u0000\u0103\u00fb\u0001\u0000\u0000\u0000\u0103\u00fc\u0001"+
		"\u0000\u0000\u0000\u0103\u00fd\u0001\u0000\u0000\u0000\u0103\u00fe\u0001"+
		"\u0000\u0000\u0000\u0104\u010d\u0001\u0000\u0000\u0000\u0105\u0106\n\t"+
		"\u0000\u0000\u0106\u0107\u0007\u0003\u0000\u0000\u0107\u010c\u0003\u001e"+
		"\u000f\n\u0108\u0109\n\b\u0000\u0000\u0109\u010a\u0007\u0004\u0000\u0000"+
		"\u010a\u010c\u0003\u001e\u000f\t\u010b\u0105\u0001\u0000\u0000\u0000\u010b"+
		"\u0108\u0001\u0000\u0000\u0000\u010c\u010f\u0001\u0000\u0000\u0000\u010d"+
		"\u010b\u0001\u0000\u0000\u0000\u010d\u010e\u0001\u0000\u0000\u0000\u010e"+
		"\u001f\u0001\u0000\u0000\u0000\u010f\u010d\u0001\u0000\u0000\u0000\u001e"+
		"\"\')/5;=BIPW_iqz\u008e\u009a\u00a0\u00b2\u00b9\u00be\u00cc\u00d3\u00d9"+
		"\u00e0\u00e8\u00ee\u0103\u010b\u010d";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}