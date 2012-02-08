use strict;
use warnings;

fbz(start => -10, end => 30);


sub fbz {
    use Scalar::Util qw( looks_like_number ); 

    my %args = @_;
    my $HOPE = 0;

    #               　 _ 　∩
    # 3.14 == π == (　ﾟ∀ﾟ)彡　おっぱい！おっぱい！
    #　                ⊂彡
    foreach my $value ( values %args ) {
        # 整数で扱うので/^3\.14$/ではない
        if ( $value =~ /^3.14/ ) {
            $HOPE++;
        }
    }
    oppai($HOPE) if $HOPE;
    
    # default or args
    my %param = (
        start => looks_like_number( $args{start} ) ? int($args{start}) :   1,
        end   => looks_like_number( $args{end}   ) ? int($args{end})   : 100,
        fz    => looks_like_number( $args{fz}    ) ? int($args{fz})    :   3,
        bz    => looks_like_number( $args{bz}    ) ? int($args{bz})    :   5,
        fbz   => looks_like_number( $args{fbz}   ) ? int($args{fbz})   :  15,
    );

    # Avoid to 'Variable "%s" will not stay shared' error.
    # In perldoc :
    #     This problem can usually be solved by making the inner subroutine anonymous,
    #     using the sub {} syntax.
    my $increment = sub {
        for ( $param{start} .. $param{end} ) {
               if ( $_ == 0 )               { print "$_\n"; }
            elsif ( $_ % $param{fbz} == 0 ) { print "FizzBuzz\n"; }
            elsif ( $_ % $param{fz}  == 0 ) { print "Fizz\n"; }
            elsif ( $_ % $param{bz}  == 0 ) { print "Buzz\n"; }
             else                           { print "$_\n"; }
        }
    };
    my $decrement = sub {
        for ( my $i = $param{start}; $i >= $param{end}; $i-- ) {
               if ( $i % $param{fbz} == 0 ) { print "FizzBuzz\n"; }
            elsif ( $i % $param{fz}  == 0 ) { print "Fizz\n"; }
            elsif ( $i % $param{bz}  == 0 ) { print "Buzz\n"; }
             else                           { print "$i\n"; }
        }
    };

    if ( $param{start} <= $param{end} ) {
        $increment->();
    } else {
        $decrement->();
    };
    
}

sub oppai {
    my $count = shift;
    print <<OPPAI x $count;
   _ 　∩
(　ﾟ∀ﾟ)彡　おっぱい！おっぱい！
  ⊂彡
OPPAI

    exit;
}

