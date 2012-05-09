#!/usr/bin/env perl
use strict;
use warnings;
use CGI;
use local::lib '/var/www/cgi-bin/extlib';
use Text::Xslate;
use Data::Section::Simple;
use Scalar::Util 'looks_like_number';

my @result = ();

my $q = CGI->new;

my $count=0;
my %param = map { $_ => $q->param($_)} $q->all_parameters;

foreach ( values %param ) {
    $count++ if $_ =~ /^3\.14$/;
}
if ($count > 0) {
    @result = oppai($count);
    render(@result);
}

my $x = $q->escapeHTML( $q->param('start') );
my $y = $q->escapeHTML( $q->param('end')   );
my %pattern = (
    start => looks_like_number($x) ? $x :   1,
    end   => looks_like_number($y) ? $y : 100,
    fz    =>  3,
    bz    =>  5,
    fbz   => 15,
);

@result = FizzBuzz();

render(@result);

sub render {
    my @result = @_;
    # Rendering
    my $vpath = Data::Section::Simple->new()->get_data_section();
    my $tx    = Text::Xslate->new( path => [$vpath] );
    print "Content-Type: text/html\n\n";
    print $tx->render('child.tx', { data => \@result });
    exit;
}

sub FizzBuzz {
    my @result;

    if ($pattern{start} < $pattern{end} ) {
        @result = increment();
    } else {
        @result = decrement();
    }
   
    return @result;
    
}

sub increment {
    my @result;
    for ( $pattern{start} .. $pattern{end} ) {
        if    ( $_ == 0 )                 { push(@result, $_ )        }
        elsif ( $_ % $pattern{fbz} == 0 ) { push(@result, "FizzBuzz") }
        elsif ( $_ % $pattern{fz}  == 0 ) { push(@result, "Fizz")     }
        elsif ( $_ % $pattern{bz}  == 0 ) { push(@result, "Buzz")     }
        else                              { push(@result, $_ )        }
    }
    
    return @result; 

}

sub decrement {
    my @result;
    for ( my $i = $pattern{start}; $i >= $pattern{end}; $i-- ) {
        if    ( $i == 0 )                 { push(@result, $i )        }
        elsif ( $i % $pattern{fbz} == 0 ) { push(@result, "FizzBuzz") }
        elsif ( $i % $pattern{fz}  == 0 ) { push(@result, "Fizz")     }
        elsif ( $i % $pattern{bz}  == 0 ) { push(@result, "Buzz")     }
        else                              { push(@result, $i )        }
    }

    return @result; 

}

sub oppai {
    my $count = shift;
    my @result;
    my $aa ="
　 _ 　∩
(　゜∀゜)彡　おっぱい！おっぱい！
　⊂彡
";
    push(@result, $aa) for 1 .. $count;
    render(@result);

}


__DATA__
@@ base.tx
<html>
<body>
: block body -> {} 
</body>
</html>

@@ child.tx
: cascade base;
: override body -> {
: for $data -> $item {
<div><pre><: $item :></pre></div>
: }
: }
